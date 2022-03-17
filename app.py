from venv import create
from web_app import create_app, db
# from app import views

if __name__ == "__main__":
	app = create_app('config')
	with app.app_context():
		db.create_all()
	app.run(debug = True)