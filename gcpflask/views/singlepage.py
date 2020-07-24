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


## Single Page Template Views --------------------------------------------------
# A single page app might want to quickly show data and contributors


@app.route("/singlepage")
def singlepage():
    return render_template("singlepage/index.html")
