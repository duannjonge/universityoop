from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer(), primary_key=True)
    name= Column(String())