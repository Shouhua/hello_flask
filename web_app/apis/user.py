from flask_restful import Resource
from flask import jsonify, make_response
from web_app.models.user import User

class UserApi(Resource):
	def get(self, id):
		user = User.query.filter_by(id=id).first()
		if user is None:
			return 404
		else:
			response = make_response(jsonify(user.serialize()), 200) 
			response.headers["Content-Type"] = "application/json"
			return response