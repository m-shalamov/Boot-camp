import pika


def cb(ch, method, properties, body):
    print(body)


user = "user"
password = "1234"
host = "localhost"
port = 5672
parameters = pika.URLParameters(f"amqp://{user}:{password}@{host}:{port}")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue="first")
channel.basic_consume(queue="first", on_message_callback=cb, auto_ack=True)
print("waiting for messages")
channel.start_consuming()
