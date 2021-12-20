from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from celery import Celery

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        data = {}
        data["email"] = request.form["email"]
        data["message"] = request.form["message"]
        duration = int(request.form["duration"])

        send_mail.apply_async(args=[data], countdown=duration)
        flash(f"Email will be sent to {data['email']} in {duration} secs")
        return redirect(url_for("index"))


mail = Mail(app)
client = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])


@client.task
def send_mail(data):
    with app.app_context():
        msg = Message(
            "Very important email",
            sender=app.config["MAIL_USERNAME"],
            recipients=[data["email"]],
        )
        msg.body = data["message"]
        mail.send(msg)


if __name__ == "__main__":
    app.run()
