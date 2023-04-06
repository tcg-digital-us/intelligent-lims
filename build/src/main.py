import json, os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

main_file_path = os.path.abspath(os.path.dirname(__file__))

def load_config():
    try:
        config_file_path = os.path.join(main_file_path, 'config.json')
        with open(config_file_path) as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

def post_to_handler(lims, data, lims_to_url):
    url = lims_to_url.get(lims)
    if not url:
        return None

    response = requests.post(url, json=data)
    return response.json()

@app.route('/intelligent-lims', methods=['POST'])
def handle_type():
    config = load_config()

    if not config:
        return jsonify({"error": "Failed to load config"}), 500

    lims_to_url = config.get('lims_to_url', {})

    try:
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
    app.run(debug=True, host='0.0.0.0', port=5002)
