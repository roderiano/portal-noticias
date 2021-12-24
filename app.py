from flask import Flask
from werkzeug.datastructures import is_immutable
from services.database import db
from flask_migrate import Migrate
from services.marshmallow import ma
from views.author import bp_authors
from views.news import bp_news

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    ma.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(bp_authors)
    app.register_blueprint(bp_news)

    return app

if __name__ == '__main__':
    app = create_app().run()