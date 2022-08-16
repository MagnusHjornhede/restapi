from flask import Flask  # __ and __ makes a python package?
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)  # __represent name of the file to init flask
    app.config['SECRET_KEY'] = 'fgfgrrtthg'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # Tell database location
    db.init_app(app)  # init database

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
