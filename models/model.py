from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

# Use declarative_base from sqlalchemy.orm
Base = declarative_base()

# Student Class
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define the relationship with Student and specify the secondary table
    students = relationship("Student", secondary="student_units")

    def __str__(self):
        return f"Unit(id: {self.id}, Name: {self.name})"

class StudentUnit(Base):
    __tablename__ = 'student_units'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    unit_id = Column(Integer, ForeignKey('units.id'), primary_key=True)

# Lecturer Class
class Lecturer(Base):
    __tablename__ ='lecturers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)

    def __str__(self):
        return f"Lecturer(id: {self.id}, Name: {self.name}, Department: {self.department})"

# # Unit Class
# class Unit(Base):
#     __tablename__ = 'units'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

#     # Define a relationship to the Student model
#     students = relationship("Student", back_populates="unit")