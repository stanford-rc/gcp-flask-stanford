import os

DATABASE = os.environ.get("FLASKAPP_DATABASE", "sqlite")

from .relational import *

if DATABASE.startswith("sqlite"):
    from .sqlite import *
