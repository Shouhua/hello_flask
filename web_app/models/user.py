from .base import Base
from web_app import db

class User(Base):
	__tablename__ = 'user'
	# User Name
	name    = db.Column(db.String(128),  nullable=False)

	# Identification Data: email & password
	email    = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(192), nullable=False)

	# Authorisation Data: role & status
	# role     = db.Column(db.SmallInteger, nullable=False)
	# status   = db.Column(db.SmallInteger, nullable=False)

	# New instance instantiation procedure
	def __init__(self, name, email, password):
			self.name     = name
			self.email    = email
			self.password = password

	def __repr__(self):
			return '<User %r>' % (self.name) 

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'email': self.email,
			'password': self.password
		}