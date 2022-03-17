from flask_restful import Resource
from flask import jsonify, request, make_response
from web_app import db
from flask import current_app as app
from web_app.models.user import User

class UserListApi(Resource):
	def post(self):
		raw_user = request.get_json()
		# validate user object
		app.logger.info('create user: %s', raw_user)
		user = User(raw_user['name'], raw_user['email'], raw_user['password'])
		db.session.add(user)
		db.session.commit()
		response = make_response(jsonify(user.serialize()), 201) 
		response.headers["Content-Type"] = "application/json"
		return response