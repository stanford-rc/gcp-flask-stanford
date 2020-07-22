from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_cors import CORS
from .database import *

import random
import sys
import os


# SERVER CONFIGURATION #########################################################


class FlaskServer(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskServer, self).__init__(*args, **kwargs)
        self.initdb()

    def initdb(self):
        """initialize the database depending on request from the user.
        """
        self.database = os.environ.get("FLASKAPP_DATABASE", "sqlite")
        self.logger.info("DATABASE: %s" % self.database)

        # Supported database options
        valid = ("sqlite", "postgres", "mysql")
        if not self.database.startswith(valid):
            self.logger.warning(
                "%s is not yet a supported type, saving to sqlite." % self.database
            )
            self.database = "sqlite"

        self.init_db()  # uses url in self.database
        self.logger.debug("Data base: %s" % self.database)


# Database functions
FlaskServer.init_db = init_db

app = FlaskServer(__name__, instance_relative_config=True)
app.config.from_object("config")

# Add the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.session_protection = "strong"

# Cors

cors = CORS(
    app,
    origins="http://127.0.0.1",
    allow_headers=[
        "Content-Type",
        "Authorization",
        "X-Requested-With",
        "Access-Control-Allow-Credentials",
    ],
    supports_credentials=True,
)

app.config["CORS_HEADERS"] = "Content-Type"

csrf = CSRFProtect(app)
