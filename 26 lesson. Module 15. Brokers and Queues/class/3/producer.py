import pika
import time
import random
import redis

cache = redis.Redis(host="localhost", port=6379)

user = "user"
password = "1234"
host = "localhost"
port = 5672
parameters = pika.URLParameters(f"amqp://{user}:{password}@{host}:{port}")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange="message", exchange_type="fanout")


for i in range(10000):
    x = random.randint(0, 100)
    print(x)
    cache_answer = cache.get(x)
    if cache_answer is not None:
        print("data is already in cache")
        continue
    channel.basic_publish(exchange="message", routing_key="", body=f"{x}")
    cache.mset({x: x})
    # time.sleep(1)
print("end")
time.sleep(100)
connection.close()
