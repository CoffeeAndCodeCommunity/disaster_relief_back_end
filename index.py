from flask import Flask
from flask import jsonify
import json
import requests
#from pymongo import MongoClient
import random

app = Flask(__name__)

smhi_url = 'https://opendata-download-warnings.smhi.se/api/version/2.json'

data ={"events": [{"id": 0, "name": "average wind speed at sea", "severity": "Moderate", "description": "Lördag kväll tillfälligt sydväst 14 m/s."}, {"id": 1, "name": "heavy snow SMHI-B", "description": "Lördag sent eftermiddag och kväll, i den västra och nordligaste delen, snö eller blötsnö som kan ge 1-4 cm. I övriga delar faller nederbörden mest som regn eller snöblandat regn.", "severity": "Hazardous"}]}

images = {"wind": "http://cdn.video.nationalgeographic.com/45/af/7613e67c456588dedde7d7da0fae/nw-dly-ds1702001-238-tornado-storm-chasing-vin-spd-op-p170629.jpg",
          "rain": "https://d1u4oo4rb13yy8.cloudfront.net/article/71489-klgwvidznp-1508409046.jpg",
          "thunder": "https://media.phillyvoice.com/media/images/05152018_lightning_stock_Pexels.2e16d0ba.fill-735x490.jpg"}

def get_smhi_data():
    req = requests.get("https://opendata-download-warnings.smhi.se/api/version/2/alerts.json").json()
    data = {"events": []}
    id_ = 0
    for alert in req["alert"]:
        print(alert)
        eventCode = list(filter(lambda e: e["valueName"] == "system_event_level_sv-SE", alert["info"]["eventCode"]))[0]
        name = eventCode["value"]
        severity = alert["info"]["severity"]
        description = alert["info"]["description"]
        event = random.choice(["wind", "rain", "thunder"])
        image = images[event]
        id_ += 1
        data["events"].append({"name": name, "severity": severity, "description": description, "id": id_, "imageUrl": image})
    return data

@app.route("/smhi")
def smhi():
    # resp = requests.get(url=smhi_url)
    # data = resp.json() 
    return app.response_class(response=json.dumps(get_smhi_data()), mimetype="application/json")

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