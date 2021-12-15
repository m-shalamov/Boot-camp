import pika
import time


user = "user"
password = "1234"
host = "localhost"
port = 5672
parameters = pika.URLParameters(f"amqp://{user}:{password}@{host}:{port}")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange="message", exchange_type="fanout")


for i in range(40):
    channel.basic_publish(exchange="message", routing_key="", body=f"{i}")
    print(i)
    time.sleep(1)
print("end")
time.sleep(100)
connection.close()
