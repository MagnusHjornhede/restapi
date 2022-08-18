from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)  # Setting up blueprint for flask app


@views.route('/')
@login_required
def home():
    return render_template("home.html")
