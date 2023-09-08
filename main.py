from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models.lecturer import Lecturer
from models.student import Student
from models.unit import Unit
from models.base import Base
import os 



DB_DIR = os.path.dirname(os.path.realpath(__file__))
conn = "sqlite:///" + os.path.join(DB_DIR, "university.db")
engine = create_engine(conn, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
