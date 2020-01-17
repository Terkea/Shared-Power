from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from app.models.base import Base

# For each model import it
import app.models.users
import app.models.tools
import app.models.booking
import app.models.returns
import app.models.invoices
import app.models.investigation
import app.models.checkout

# establish the connection
# the engine can be easily changed, for know I left it as SQLite since it's easier when working on a group project
engine = create_engine('sqlite:///SharedPower.sqlite')
# map the tables
Base.metadata.create_all(bind=engine)
# create the session
Session = sessionmaker(bind=engine)

# GLOBAL VARIABLE
session = Session()