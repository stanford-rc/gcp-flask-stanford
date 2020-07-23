from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging
import os

logging.basicConfig(level=logging.INFO)
bot = logging.getLogger("gcpflask.database")

Base = declarative_base()


def init_db(self):
    """initialize the database, with the default database path or custom of
       the format sqlite:///flaskapp.sqlite
    """

    # Database Setup, use default if uri not provided
    if self.database == "sqlite":
        self.database = "sqlite:///flaskapp.sqlite"
        database_file = os.getenv("FLASKAPP_DATABASE_FILE")
        if database_file is not None:
            self.database = "sqlite:///%s" % database_file

    bot.info("Database located at %s" % self.database)
    self.engine = create_engine(self.database, convert_unicode=True)
    self.session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    )

    Base.query = self.session.query_property()

    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from . import models

    Base.metadata.create_all(bind=self.engine)
    self.Base = Base
