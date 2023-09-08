from sqlalchemy import Column, Integer, String, ForeignKey  # Import ForeignKey here
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define a one-to-many relationship with the Unit entity
    unit_id = Column(Integer, ForeignKey('units.id'))
    units = relationship("Unit", back_populates="students")

class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define a reverse one-to-many relationship with the Student entity
    students = relationship("Student", back_populates="units")
