from website import db
from website.models import User

db.create_all()

user_1 = User(username = "Jack", email = "jack@gmail.com", password = "1234")
user_2 = User(username = "Tom", email = "tom@gmail.com", password = "1234")

db.session.add(user_1)
db.session.add(user_2)

db.session.commit()