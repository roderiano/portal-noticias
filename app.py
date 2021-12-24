from flask import Flask
from services.database import db
from flask_migrate import Migrate
from services.marshmallow import ma

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    ma.init_app(app)
    migrate = Migrate(app, db)

    app.run()

if __name__ == '__main__':
    create_app()