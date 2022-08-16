from flask import Flask  # __ and __ makes a python package?
from flask_sqlalchemy import SQLAlchemy
from os import path

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
    # First make sure modes load up before continue
    from .models import User, Note
    create_database(app)
    return app


def create_database(app):  # check if database is already created
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)  # need to inform for which app alchemy is creating app for
        print('Database created')
