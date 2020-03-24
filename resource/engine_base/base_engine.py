from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
engine = create_engine('sqlite:///chinook.db', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))

_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()
# Base.query = db_session.query_property()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()