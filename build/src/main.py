import os, toml, re
import requests
from flask import Flask, request, jsonify
from Config import app_host, base_urls, ConfigGetError

app = Flask(__name__)

class LimsUrlNotFoundError(Exception):
    pass

class LimsTypeError(Exception):
    pass

def post_to_handler(lims, data, base_urls):
    """
    Raises: LimsUrlNotFoundError
    """

    url = base_urls.get(lims)
    if not url:
        raise LimsUrlNotFoundError(f"URL not found for LIMS type {lims}")

    response = requests.post(url, json=data)
    return response.json()

@app.route('/intelligent-lims', methods=['POST'])
def handle_type():
    try:
        base_url_list = base_urls()
        data = request.json
        lims = data.get('lims')

        if lims is None or lims not in base_url_list:
            raise LimsTypeError("Unsupported LIMS type")

        response = post_to_handler(lims, data, base_url_list)
        return jsonify(response)
    except (
        ValueError,
        ConfigGetError,
        LimsUrlNotFoundError,
        LimsTypeError
    ) as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    try:
        _host, _port = app_host()
        app.run(debug=True, host=_host, port=_port)
    except ConfigGetError as e:
        print(str(e))