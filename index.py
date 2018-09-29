from flask import Flask
from flask import jsonify
import json
import requests

app = Flask(__name__)

smhi_url = 'https://opendata-download-warnings.smhi.se/api/version/2.json'

data ={"events": [{"id": 0, "name": "average wind speed at sea", "severity": "Moderate", "description": "Lördag kväll tillfälligt sydväst 14 m/s."}, {"id": 1, "name": "heavy snow SMHI-B", "description": "Lördag sent eftermiddag och kväll, i den västra och nordligaste delen, snö eller blötsnö som kan ge 1-4 cm. I övriga delar faller nederbörden mest som regn eller snöblandat regn.", "severity": "Hazardous"}]}

@app.route("/smhi")
def smhi():
    # resp = requests.get(url=smhi_url)
    # data = resp.json() 
    return app.response_class(response=json.dumps(data), mimetype="application/json")

@app.route("/")
def hello():
    return "Hello world!"


