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
@app.route("/modern")
def modern_home():
    return render_template("modern/home.html")


@app.route("/modern/register", methods=["GET", "POST"])
def modern_register():
    """Register a user for your application using the RegistrationForm->forms.py
    """
    # If the user is already authenticated, redirect to index view
    if current_user.is_authenticated:
        return redirect(url_for("modern_home"))

    # Otherwise, prepare a RegistrationForm to validate on submit
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        app.session.add(user)
        app.session.commit()
        flash("Congratulations, you are now a registered user!")

        # Redirect the user to login when they have registered
        return redirect(url_for("modern_login"))
    return render_template("modern/register.html", title="Register", form=form)


@app.route("/modern/login", methods=["GET", "POST"])
def modern_login():
    """Allow a user to login to the cardinal view
    """
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("modern_login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("modern_home"))
    return render_template("modern/login.html", title="Sign In", form=form)
