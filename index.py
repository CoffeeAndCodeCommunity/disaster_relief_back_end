from flask import Flask
from flask import jsonify
import json
import requests
from pymongo import MongoClient

app = Flask(__name__)

smhi_url = 'https://opendata-download-warnings.smhi.se/api/version/2.json'

data ={"events": [{"name": "average wind speed at sea", "severity": "Moderate", "description": "Lördag kväll tillfälligt sydväst 14 m/s."}, {"name": "heavy snow SMHI-B", "description": "Lördag sent eftermiddag och kväll, i den västra och nordligaste delen, snö eller blötsnö som kan ge 1-4 cm. I övriga delar faller nederbörden mest som regn eller snöblandat regn.", "severity": "Hazardous"}]}

@app.route("/smhi")
def smhi():
    # resp = requests.get(url=smhi_url)
    # data = resp.json() 
    return app.response_class(response=json.dumps(data), mimetype="application/json")

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/mongodb")
def mongo():
    client = MongoClient('localhost', 27017)
    # db = client.get_default_database()
    db = client['mydb']
    events = db['events']
    events.insert_many(data['events'])
    query = {'severity': 'Moderate' }
    cursor = events.find(query)
    ourdata = []
    for doc in cursor:
        ourdata += doc
    return app.response_class(response=json.dumps(ourdata), mimetype="application/json")