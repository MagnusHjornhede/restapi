from flask import Blueprint

auth = Blueprint('auth', __name__)  # Setting up blueprint for flask app


@auth.route('/login')
def login():
    return "<p>Login<p>"


@auth.route('/logout')
def logout():
    return "<p>Logout<p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign up<p>"
