import pika
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time

visited = set()
page_count = 0
MAX_PAGES = 10

# -------------------------------
# Create unique folder per worker
# -------------------------------
worker_id = str(os.getpid())  # unique process ID
folder_name = f"pages_worker_{worker_id}"
os.makedirs(folder_name, exist_ok=True)

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.queue_declare(queue='url_queue', durable=True)


def callback(ch, method, properties, body):
    global page_count

    url = body.decode()

    # Skip if already visited or limit reached
    if url in visited or page_count >= MAX_PAGES:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    print(f"[Worker {worker_id}] Fetching: {url}")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        html = response.text

    except requests.exceptions.RequestException:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    # Save HTML file inside worker-specific folder
    page_count += 1
    filename = f"{folder_name}/page_{page_count}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[Worker {worker_id}] Saved: {filename}")

    # Extract links
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")

    for tag in links:
        href = tag.get("href")
        if href:
            absolute_link = urljoin(url, href)

            channel.basic_publish(
                exchange='',
                routing_key='url_queue',
                body=absolute_link,
                properties=pika.BasicProperties(
                    delivery_mode=2,
                )
            )

    visited.add(url)

    print(f"[Worker {worker_id}] Extracted {len(links)} links\n")

    time.sleep(3)

    ch.basic_ack(delivery_tag=method.delivery_tag)


# Fair dispatch
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='url_queue', on_message_callback=callback)

print(f"Worker {worker_id} waiting for messages...")
channel.start_consuming()
