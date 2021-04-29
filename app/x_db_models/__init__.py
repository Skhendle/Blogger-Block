from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()

# XXX: Development imports
from app.x_db_models.user import User
from app.x_db_models.post import Post
from app.x_db_models.requests import Requests

# We are using ORM from sqlalchemy so that we 
# can have a better representation of our relationships

engine = create_engine('sqlite:///:memory:', echo=False)

engine = create_engine('sqlite:///test_db.db', echo=False)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# XXX: Production imports
# Running commands in the parent folder of current file

# from x_db_models.user import User
# from x_db_models.post import Post
# from x_db_models.requests import Requests

# engine = create_engine("mysql://blogger:Blogger12345#@localhost/blogger", echo=False)
