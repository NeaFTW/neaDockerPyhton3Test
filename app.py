#! /usr/bin/env python3.5

import flask
from flask import Flask
app = Flask(__name__)

import os
import json

@app.route("/")
def hello():
    return "This is a server for DeVops"

@app.route("/v1/groupname")
def toto():
    jsonresult = {}
    jsonresult["data"] = {}
    jsonresult["data"]["groupname"] = os.environ['GROUPNAME']
    jsonresult["result"] = "success"
    #jsonresult["data"]["groupname"] = os.getenv('GROUPNAME', "Strontium")


    print(jsonresult)
    return flask.jsonify(jsonresult)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
