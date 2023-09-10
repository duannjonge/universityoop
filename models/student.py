from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .lecturer import Lecturer
from .associations import student_unit_association

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define a many-to-many relationship with the Unit entity
    units = relationship("Unit", secondary=student_unit_association, back_populates="students")

    def __init__(self, name):
        self.name = name

    def add_unit(self, unit):
        self.units.append(unit)

    def __str__(self):
        return f"Student(id: {self.id}, Name: {self.name})"

# Define a reverse one-to-many relationship with the Lecturer entity
# This should be defined outside the Student class
Lecturer.students = relationship(Student, back_populates="lecturer")
