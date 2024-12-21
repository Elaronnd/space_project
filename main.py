from flask import Flask, render_template, request
from space_api import get_space_json, get_space_info

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route(rule="/image")
def image():
    date = None if request.args.get("date") == "" else request.args.get("date")
    data = get_space_json(date=date)
    data = get_space_info(data)
    return render_template("index.html",
                           multiinfo=data[1] if data[0] is list else None,
                           info=data[1] if data[0] is dict else None)


app.run()
