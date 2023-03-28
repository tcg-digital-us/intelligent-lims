import json
import random
from flask import Flask, request

def release_model (data):
   #random.seed(42)
   score = random.random()
   score_data = {"batch_id": data['batch_id'],
                 "batch_release_score": score}
   json_data = json.dumps(score_data)
   return json_data


app = Flask(__name__)

@app.route('/batch_release', methods=['POST'])
def result():
    if request.method == 'POST':
        data = request.get_json(force=True)
        json_data = release_model(data)
        return json_data

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
