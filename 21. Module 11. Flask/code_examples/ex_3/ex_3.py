from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = '2688088b53e6e0116a1ddb59f72db9d1'
links = [
    {
        "name": "Andrew Black",
        "year": "1998",
        "url": "https://en.wikipedia.org/wiki/Andrew"
    },
    {
        "name": "Michael Red",
        "year": "2010",
        "url": "https://en.wikipedia.org/wiki/Michael"
    },
    {
        "name": "Bob Dark",
        "year": "2020",
        "url": "https://en.wikipedia.org/wiki/Bob_(given_name)"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", links=links)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Registration", form = form)

if __name__ == "__main__":
    app.run(debug=True)