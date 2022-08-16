from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)  # Setting up blueprint for flask app


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing")


@auth.route('/logout')
def logout():
    return "<p>Logout<p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # Add user to database
            pass

    return render_template("sign_up.html")
