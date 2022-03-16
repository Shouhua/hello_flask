from flask_restful import Resource
from flask import jsonify, request

class Hello(Resource):
	def get(self):
		return jsonify({'message': 'hello world'})

	def post(self):
		data = request.get_json()
		return jsonify({'data': data})