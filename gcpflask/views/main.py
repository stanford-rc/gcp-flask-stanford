from flask import (
    redirect,
    render_template,
    url_for,
    flash,
)
from flask_login import logout_user

from ..server import app, login_manager
from ..forms import LoginForm, RegistrationForm
from ..database.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.context_processor
def inject_configvars():
    """inject global configuration variables (title, twitter, etc.) into
       pages from config.py
    """
    print(app.config.keys())
    items = {}
    for key in ["TITLE", "TWITTER", "GITHUB_REPOSITORY"]:
        if key in app.config and app.config[key]:
            items[key] = app.config[key]
    print(items)
    return items


# Root login URL


@app.route("/")
def index():
    return render_template("base/index.html")


## Shared Users Views -----------------------------------------------------------------


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been successfully logged out.")
    return redirect(url_for("index"))
