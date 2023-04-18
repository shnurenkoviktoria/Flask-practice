import csv
from statistics import mean

import flask
import requests
from faker import Faker

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/requirements/")
def task1():
    with open("requirements.txt", "r") as fi:
        requirements = fi.read()
    return flask.render_template("TASK1.html", requirements=requirements)


@app.route("/users/generate", methods=["GET"])
def task2():
    dict1 = {}
    fake = Faker()
    num = 100
    try:
        num = int(flask.request.args['num'])
    except(Exception,):
        pass

    for i in range(num):
        dict1[fake.name()] = fake.ascii_company_email()
    return flask.render_template("TASK2.html", dict1=dict1, num=num)


@app.route("/mean/")
def task3():
    with open("hw.csv") as fi:
        reader = list(csv.reader(fi))
        reader.pop(0)
        height_average = mean([float(reader[i][1]) for i in range(len(reader) - 1)]) * 2.54
        weight_average = mean([float(reader[i][2]) for i in range(len(reader) - 1)]) / 2.205

    return flask.render_template("TASK3.html", height_average=height_average, weight_average=weight_average)


@app.route("/space/")
def task4():
    request = requests.get("http://api.open-notify.org/astros.json")
    number = request.json()["number"]
    return flask.render_template("TASK4.html", number=number)


if __name__ == '__main__':
    app.run()
