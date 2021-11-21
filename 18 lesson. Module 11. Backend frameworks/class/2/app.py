from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    count = db.Column(db.Integer)

    def __init__(self, name, count) -> None:
        self.name = name
        self.count = count

    def __str__(self) -> str:
        return f"{self.id}"


db.create_all()


@app.route("/")
def home():
    return "Hello"


@app.route("/users/<name>")
def get_data(name):
    user = User.query.filter_by(name=name).first()
    user.count += 1
    db.session.commit()
    return jsonify({"name": user.name, "count": user.count})


@app.route("/user", methods=["POST"])
def add():
    data = request.json
    user = User(name=data["name"], count=data["count"])
    db.session.add(user)
    db.session.commit()
    return jsonify(data)


if __name__ == "__main__":
    app.run()
