from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<div>HOME</div>"

@app.route("/about")
def about():
    return "<div>ABOUT</div>"


if __name__ == "__main__":
    app.run(debug=True)

