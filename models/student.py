from sqlalchemy import Column, Integer, String, ForeignKey  # Import ForeignKey here
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit=Column(String)

    # Define a one-to-many relationship with the Unit entity
    #Gets the unit the student is taking
    unit_id = Column(Integer, ForeignKey('units.id'))
    units = relationship("Unit", back_populates="students")
    
## Object Operations

    def __init__(self,name):
        self.name=name

    # helper methods 

    def add_unit(self,unit):
        self.units.append(unit)

    
    def __str__(self):

        return f"Student(id:{self.id}Name:{self.name} Unit:{self.unit})"
    
    # Define a reverse one-to-many relationship with the Student entity
    students = relationship("Student", back_populates="units")
