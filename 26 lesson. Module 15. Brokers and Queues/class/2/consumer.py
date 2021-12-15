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
channel.exchange_declare(exchange="message", exchange_type="fanout")
result = channel.queue_declare(queue="")
queue_name = result.method.queue
channel.queue_bind(exchange="message", queue=queue_name)
channel.basic_consume(queue=queue_name, on_message_callback=cb, auto_ack=True)
print("waiting for messages")
channel.start_consuming()
