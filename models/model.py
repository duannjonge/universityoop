from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

# Use declarative_base from sqlalchemy.orm
Base = declarative_base()

# Student Class
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit_id = Column(Integer, ForeignKey('units.id'))  # Define a foreign key relationship to the 'units' table
 
    unit = relationship("Unit", back_populates="students")

    def __str__(self):
        return f"Student(id: {self.id}, Name: {self.name}, Unit: {self.unit.title if self.unit else None})"


# Lecturer Class
class Lecturer(Base):
    __tablename__ ='lecturers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)

    def __str__(self):
        return f"Lecturer(id: {self.id}, Name: {self.name}, Department: {self.department})"

# Unit Class
class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    
    students = relationship("Student", back_populates="unit")

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Unit(id: {self.id}, Title: {self.title})"
