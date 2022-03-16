import flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from web_app.apis.hello import Hello
from web_app.apis.square import Square

app = flask.Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

# db.create_all()

# api = Api(app, prefix="/api/v0.1")
api = Api(app)

api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
