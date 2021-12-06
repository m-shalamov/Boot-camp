from application.app import db

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