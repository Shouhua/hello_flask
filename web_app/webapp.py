# Entry point for the application.
from . import create_app, db    # For application discovery by the 'flask' command.

app = create_app('config')
with app.app_context():
	db.create_all()
# print(app.config)