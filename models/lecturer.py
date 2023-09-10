from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .associations import student_unit_association
class Lecturer(Base):
         __tablename__ ='lecturers'
         id = Column(Integer(), primary_key=True)
         name = Column(String())
         department=Column(String())
         units = relationship("Unit", secondary= student_unit_association,back_populates="students")

         def __init__(self,name):
                  self.name=name

         def write_unit(self,unit):
             unitclass=Lecturer(unit)
             self.writeunits.append(unitclass)
             unit.add_unitmain(unitclass)
             return unitclass
         


         def __str__(self):

            return f"Student(id:{self.id}Name:{self.name} Unit:{self.unit})"