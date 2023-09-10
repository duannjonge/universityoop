# for one to one or one to many or many to many rships
#join table

#foreign keys :unit id
from sqlalchemy import Table, Column, Integer, ForeignKey
from .student import Student 

from .base import Base

student_unit_association = Table(
    'student_unit_association',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('unit_id', Integer, ForeignKey('units.id')),
    extend_existing=True,
)

# student_unit_association=Table(
#     'student_unit_association',
#     Base.metadata,
#     Column('student_id',Integer,ForeignKey('students.id')),

#     Column('unit_id',Integer,ForeignKey('units.id')),
#     extend_existing=True,



# )
