import os, toml, re
import requests
from flask import Flask, request, jsonify
from Config import app_host, base_urls, ConfigNotFoundError

app = Flask(__name__)

def post_to_handler(lims, data, lims_to_url):
    url = lims_to_url.get(lims)
    if not url:
        return None

    response = requests.post(url, json=data)
    return response.json()

@app.route('/intelligent-lims', methods=['POST'])
def handle_type():
    try:
        lims_to_url = base_urls()
        data = request.json
        lims = data.get('lims')

        if lims in lims_to_url:
            response = post_to_handler(lims, data, lims_to_url)
            if response:
                return jsonify(response)
            else:
                return jsonify({"error": "URL not found for LIMS type"}), 400
        else:
            return jsonify({"error": "Unsupported LIMS type"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    try:
        _host, _port = app_host()
        app.run(debug=True, host=_host, port=_port)
    except ConfigNotFoundError as e:
        print(str(e))