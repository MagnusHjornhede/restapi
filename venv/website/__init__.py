from flask import Flask  # __ and __ makes a python package?


def create_app():
    app = Flask(__name__)  # __represent name of the file to init flask
    app.config['SECRET_KEY'] = 'fgfgrrtthg'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
