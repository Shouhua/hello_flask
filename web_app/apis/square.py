from flask_restful import Resource
from flask import jsonify
from flask import current_app as app

class Square(Resource):
	def get(self, num):
		app.logger.info("Request %i**2: %i", num, num**2)
		return jsonify({'square': num**2})