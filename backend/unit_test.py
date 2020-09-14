import unittest
import json
from flask import jsonify
from app import app

class UnitTest(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()

	def test_get_data(self):
		res = self.app.get('/getData', headers={"Content-Type": "application/json"})
		data = res.json['data']['package']
		print(len(data))

		self.assertTrue(len(data) > 1)
	
	def test_add_package(self):
		new_package = {
			"pickup": "Joo Koon",
			"deliver": "Changi Airport",
			"datetime": "13/09/2020 10:00",
			"status": "To Be Picked Up"
		}
		res = self.app.post('/addPackage', headers={"Content-Type": "application/json"}, data=json.dumps(new_package))
		with open("data/data.json") as f:
			data = json.load(f)

			# Asserts new package is subset of json data
			self.assertDictContainsSubset(new_package, data['package'][-1])
		

	def test_update_status(self):
		with open("data/data.json") as f:
			data = json.load(f)
			res = self.app.put('/updateStatus/' + str(data['package'][-1]['id']), headers={"Content-Type": "application/json"}, 
												data=json.dumps({"newStatus": "Delivered"}))
			new_package = res.json['data']['package'][-1]
			self.assertTrue(new_package['status'] == 'Delivered')

if __name__ == '__main__':
    unittest.main()