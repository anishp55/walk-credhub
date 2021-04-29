from flask import json
from app import app
from flask import jsonify
import json
import os

@app.route('/credhub_info')
def enter():
    services = json.loads(os.getenv("VCAP_SERVICES"))
    print(type(services))
    if "credhub" in services:
        return jsonify(services["credhub"])
    else:
        return "credhub service instances found"

@app.route("/health", methods=['GET'])
@app.route("/healthz", methods=['GET'])
def health():
    return "OK"