from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Lecturer(Base):
         __tablename__ = 'lecturers'
         id = Column(Integer(), primary_key=True)
         name = Column(String())
         department=Column(String())