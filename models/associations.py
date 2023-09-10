# for one to one or one to many or many to many rships
#join table

#foreign keys :unit id
from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

student_unit_association=Table(
    'student_unit_association',
    Base.metadata,
    Column('student_id',Integer,ForeignKey('student.id')),

    Column('unit_id',Integer,ForeignKey('unit.id')),
    extend_existing=True,



)
