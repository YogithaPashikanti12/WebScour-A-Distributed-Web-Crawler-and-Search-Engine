# producer.py

import pika

# Seed URLs
SEED_URLS = [
    "https://www.python.org",
    "https://books.toscrape.com"
]

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# Declare durable queue
channel.queue_declare(queue='url_queue', durable=True)

# Publish seed URLs
for url in SEED_URLS:
    channel.basic_publish(
        exchange='',
        routing_key='url_queue',
        body=url,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
        )
    )
    print(f"[Producer] Sent: {url}")

print("All seed URLs sent.")

connection.close()

