#main.py
# write test cases for output

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models.lecturer import Lecturer
from models.student import Student
from models.unit import Unit
from models.base import Base
import os 



DB_DIR = os.path.dirname(os.path.realpath(__file__))
conn = "sqlite:///" + os.path.join(DB_DIR, "university.db")
engine = create_engine(conn, echo=True)

#bind connection when main is run
Session = sessionmaker(bind=engine)
session = Session()


# creating the tables 
Base.metadata.create_all(engine) 

# student1=Student(name='Branden',unit='Computer Science')
# Lecturer1=Lecturer(name='John',department='Engineering')

student1='Branden','Computer Science'
lecturer1='John','Engineering'


# student2=Student(name='Thomas',unit='Accounts')
# Lecturer2=Lecturer(name='Clarkson',department='Accounting')

student2='Thomas','Accounts'
lecturer2='Clarkson','Accounting'



# unit1=Unit('Computer Science')
unit1='Computer Science'

# validate / assumpation handling 
# object creation / record insert to the db table 
student1=session.query(Student).filter_by(name=student1).first()
if not student1:
    student1 = Student(student1)


lecturer1=session.query(Lecturer).filter_by(name=lecturer1).first()
if not lecturer1:
    lecturer1 = Lecturer(lecturer1)

unit1=session.query(Unit).filter_by(name=unit1).first()
if not unit1:
    unit1 = Unit(unit1)



session.close()

if __name__ == '__main__':
    cli()