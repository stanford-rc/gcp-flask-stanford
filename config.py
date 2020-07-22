from os import environ, path
from secrets import token_hex

# **variables must be in all uppercase, rendered to lowercase in templates**

# The title of your application
TITLE = "Stanford GCP Flask Application"

# Social network aliases, comment out to leave any out
TWITTER = "vsoch"
# YOUTUBE = "username"
# FACEBOOK = "usename"

# Only displays on index navigation page
GITHUB_REPOSITORY = "https://github.com/stanford-rc/gcp-flask-stanford"

# DO NOT EDIT BELOW THIS LINE ##################################################

__basedir = path.abspath(path.dirname(__file__))

# Main
DEBUG = False

# Secrets
SECRET_KEY = environ.get("FLASK_SECRET_KEY", token_hex(64))
