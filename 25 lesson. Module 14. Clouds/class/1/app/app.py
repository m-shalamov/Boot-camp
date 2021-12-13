from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def ping():
    return socket.gethostbyname(socket.gethostname()), 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
