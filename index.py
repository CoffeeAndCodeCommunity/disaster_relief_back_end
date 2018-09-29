from flask import Flask
from flask import jsonify
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/events")
def events():
    data = {"events": [{"name": "name1"}, {"name": "name2"}]}
    return app.response_class(response=json.dumps(data), mimetype="application/json")

smhi_url = 'https://opendata-download-warnings.smhi.se/api/version/2.json'

@app.route("/smhi")
def smhi():
    resp = requests.get(url=smhi_url)
    data = resp.json() 
    print(data)
    return app.response_class(response=json.dumps(data), mimetype="application/json")

