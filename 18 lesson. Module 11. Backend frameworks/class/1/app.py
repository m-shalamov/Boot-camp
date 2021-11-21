from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


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
def home():
    return render_template("index.html", links=links)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/cities/<city>")
def data(city):
    def get_coords(city: str) -> list:
        coords = ''
        response = requests.get("https://nominatim.openstreetmap.org/search", params={"format":"json", "city":city})
        if response.status_code == 200:
            answer = response.json()
            if len(answer) > 0:
                coords = f'{answer[0]["lat"]}, {answer[0]["lon"]}'
        return coords

    return render_template("coords.html", city=request.view_args["city"], coord=get_coords(request.view_args["city"]))

if __name__ == "__main__":
    app.run()
###############################
#Для любого введеного города вернуть его координаты
#Результирующий html: London: 45, 0
