from flask import render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, current_user
from website.forms import RegistrationForm, LoginForm
from website import app, db, bcrypt
from website.models import User

links = [
    {
        "name": "Andrew Black",
        "year": "1998",
        "url": "https://en.wikipedia.org/wiki/Andrew",
    },
    {
        "name": "Michael Red",
        "year": "2010",
        "url": "https://en.wikipedia.org/wiki/Michael",
    },
    {
        "name": "Bob Dark",
        "year": "2020",
        "url": "https://en.wikipedia.org/wiki/Bob_(given_name)",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", links=links)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pass = bcrypt.generate_password_hash(form.password.data)
        user = User(
            username=form.username.data, email=form.email.data, password=hash_pass
        )
        db.session.add(user)
        db.session.commit()
        flash("You have been registrated", "success")
        return redirect(url_for("home"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash("Wrong credentials", "error")

    return render_template("login.html", form=form)

