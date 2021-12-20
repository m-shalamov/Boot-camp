from celery import Celery
import time

app = Celery("task", backend="rpc://", broker="pyamqp://user:1234@localhost:5672")


@app.task
def add(x, y):
    time.sleep(10)
    return x + y
