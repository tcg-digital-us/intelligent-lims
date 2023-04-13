"""
file: main.py
author: Anthony Mesa


"""

from flask import Flask, request, jsonify
from microservices.ReleaseScore import ReleaseScore, ReleaseScoreError
from Config import app_host, ConfigGetError
from PayloadValidator import PayloadValidator, PayloadValidationError
from storage.RecordStore import RecordStore, RecordStoreError
from actions.ActionHandler import handle_action, ActionError

# setup flask app and datastore

app = Flask(__name__)
with app.app_context():
    RecordStore.initialize(_app=app)

# setup routes

@app.route('/intelligent-lims', methods=['POST'])
def get_score():
    try:
        payload = PayloadValidator().validate_payload(request.json)
        result = handle_action(payload["action"], payload["content"])
        payload["result"] = result
        return jsonify(payload)
    except PayloadValidationError or ActionError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    try:
        _host, _port = app_host()
        app.run(debug=True, host=_host, port=_port)
    except ConfigGetError as e:
        print(str(e))
