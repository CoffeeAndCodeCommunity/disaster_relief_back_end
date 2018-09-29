from flask import Flask
from flask import jsonify
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/events")
def events():
    data = {"events": [{"name": "name1"}, {"name": "name2"}]}
    return app.response_class(response=json.dumps(data), mimetype="application/json")
