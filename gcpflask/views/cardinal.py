from flask import (
    redirect,
    render_template,
    url_for,
    session,
    flash,
)
from flask_login import current_user, login_user, logout_user, login_required

from ..server import app, login_manager
from ..forms import LoginForm, RegistrationForm
from ..database.models import User


## Cardinal Template Views -----------------------------------------------------
# These urls demonstrate the Stanford cardinal theme


@login_required
@app.route("/cardinal")
def cardinal_home():
    return render_template("cardinal/home.html")


@login_required
@app.route("/cardinal/wide")
def cardinal_wide():
    return render_template("cardinal/wide.html")


@login_required
@app.route("/cardinal/left-sidebar")
def cardinal_leftside():
    return render_template("cardinal/left-sidebar.html")


@login_required
@app.route("/cardinal/right-sidebar")
def cardinal_rightside():
    return render_template("cardinal/right-sidebar.html")


@login_required
@app.route("/cardinal/no-sidebars")
def cardinal_nosides():
    return render_template("cardinal/no-sidebars.html")


@login_required
@app.route("/cardinal/two-sidebars")
def cardinal_twosides():
    return render_template("cardinal/two-sidebars.html")


@app.route("/cardinal/register", methods=["GET", "POST"])
def register():
    """Register a user for your application using the RegistrationForm->forms.py
    """
    # If the user is already authenticated, redirect to index view
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    # Otherwise, prepare a RegistrationForm to validate on submit
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        app.session.add(user)
        app.session.commit()
        flash("Congratulations, you are now a registered user!")

        # Redirect the user to login when they have registered
        return redirect(url_for("login"))
    return render_template("users/register.html", title="Register", form=form)


@app.route("/cardinal/login", methods=["GET", "POST"])
def login():
    """Allow a user to login to the cardinal view
    """
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("users/login.html", title="Sign In", form=form)
