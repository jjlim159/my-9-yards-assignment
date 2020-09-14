from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/getData')
def getdata():
	with open("data/data.json") as f:
		data = json.load(f)
	
	res = {}
	res['status'] = 200
	res['data'] = data
	
	return jsonify(res)

@app.route('/updateStatus/<id>', methods=['PUT'])
def updateStatus(id):
	req_data = request.get_json()

	with open("data/data.json") as f:
		data = json.load(f)
		for i in data['package']:
			if i['id'] == int(id):
				i['status'] = req_data['newStatus']
				break

	with open("data/data.json", "w+") as f:
		json.dump(data, f)

	res = {}
	res['status'] = 200
	res['data'] = data

	return res

@app.route("/addPackage", methods=['POST'])
def addPackage():
	req_data = request.get_json()
	req_data['status'] = 'To Be Picked Up'

	res = {}
	res['status'] = 200

	with open("data/data.json") as f:
		data = json.load(f)
		req_data['id'] = len(data['package']) + 1
		data['package'].append(req_data)

	with open("data/data.json", "w+") as f:
		json.dump(data, f)

	return res

if __name__ == "__main__":
	app.run(debug=True)