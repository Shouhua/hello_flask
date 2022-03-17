import flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
	app = flask.Flask(__name__, instance_relative_config=True)
	app.config.from_object(config)

	try:
		app.config.from_pyfile('config.py')
	except FileNotFoundError:
		pass

	from flask_restful import Api
	api = Api(app, prefix="/api/v0.1")

	from web_app.apis.hello import Hello
	from web_app.apis.square import Square
	from web_app.apis.user import UserApi
	from web_app.apis.user_list import UserListApi

	api.add_resource(Hello, '/')
	api.add_resource(Square, '/square/<int:num>')
	api.add_resource(UserApi, '/user/<id>')
	api.add_resource(UserListApi, '/user')

	db.init_app(app)
	return app
