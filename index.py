from flask import Flask
from flask import jsonify
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/events")
def events():
    return app.response_class(response=json.dumps({"name": "hej"}), mimetype="application/json")