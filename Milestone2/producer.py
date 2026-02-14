import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# Declare queue
channel.queue_declare(queue='url_queue', durable=True)

# Seed URL
# seed_url = "https://www.python.org"
seed_url = "https://www.example.com"
# seed_url = "https://www.whatsapp.com"

# Send message
channel.basic_publish(
    exchange='',
    routing_key='url_queue',
    body=seed_url,
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)

print("Sent:", seed_url)

connection.close()


# import pika

# # Connect to RabbitMQ server
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters('localhost')
# )

# channel = connection.channel()

# # Declare queue
# channel.queue_declare(queue='url_queue', durable=True)

# # Seed URLs
# seed_urls = [
#     "https://www.python.org",
#     "https://docs.python.org",
#     "https://pypi.org",
#     "https://www.djangoproject.com"
# ]

# # Send each URL separately
# for url in seed_urls:
#     channel.basic_publish(
#         exchange='',
#         routing_key='url_queue',
#         body=url.encode(),  # convert to bytes
#         properties=pika.BasicProperties(
#             delivery_mode=2
#         )
#     )
#     print("Sent:", url)

# connection.close()

