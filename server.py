from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root_route():
    if request.method == "GET":
        return "Please, choose one of them and add to uri:/anton, /dima or /bogdan"

@app.route("/anton", methods=["GET"])
def anton():
    if request.method == "GET":
        anton_json = {
            "rost": 180,
            "wes": 75,
            "name": "Anton",
            "l_name": "O"
        }
        return json.dumps(anton_json)

@app.route("/bogdan", methods=["GET"])
def bogdan():
    if request.method == "GET":
        bogdan_json = {
            "rost": 170,
            "wes": 100,
            "name": "Bogdan",
            "l_name": "O"
        }
        return json.dumps(bogdan_json)

@app.route("/dima", methods=["GET"])
def dima():
    if request.method == "GET":
        dima_json = {
            "rost": 190,
            "wes": 100,
            "name": "Di",
            "l_name": "ma"
        }
        return json.dumps(dima_json)

@app.route("/<int:number>")
def secret(number):
    number = str(number)
    return "Hello, you are in secret page {}.".format(number)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000)

