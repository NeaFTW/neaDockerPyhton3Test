#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import flask
from flask import Flask
app = Flask(__name__)

import os
import json

@app.route("/")
def hello():
    return "This is a server for DeVops"

@app.route("/v1/GROUPNAME")
def toto():
    jsonresult = {}
    jsonresult["result"] = "success"
    jsonresult["data"] = os.environ['GROUPNAME']

    print(jsonresult)
    return flask.jsonify(jsonresult)

if __name__ == "__main__":
    app.run()
