from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from app.models.base import Base

# For each model import it
import app.models.User

# establish the connection
engine = create_engine('sqlite:///database.sqlite')
# map the tables
Base.metadata.create_all(bind=engine)
# create the session
Session = sessionmaker(bind=engine)

# GLOBAL VARIABLE
session = Session()
