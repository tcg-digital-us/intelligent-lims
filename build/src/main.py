from flask import Flask, request, jsonify
from HandlerFactory import HandlerFactory

app = Flask(__name__)
handler_factory = HandlerFactory()

@app.route('/releaseScore', methods=['POST'])
def handle_type():
	try:
		data = request.json
		type = data.get('sdcid')
		handler = handler_factory.get_handler(type)
		result = handler.handle(data)
		return jsonify({"data": data, "releaseScore": result})
	except ValueError as e:
		return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5002)