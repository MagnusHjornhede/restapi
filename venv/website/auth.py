from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)  # Setting up blueprint for flask app


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing")


@auth.route('/logout')
def logout():
    return "<p>Logout<p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")
