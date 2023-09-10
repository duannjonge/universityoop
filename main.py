#main.py
# write test cases for output

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models.lecturer import Lecturer
from models.student import Student
from models.unit import Unit
from models.associations import student_unit_association
from models.base import Base
import os 



# DB_DIR = os.path.dirname(os.path.realpath(__file__))
# conn = "sqlite:///" + os.path.join(DB_DIR, "university.db")
engine = create_engine("sqlite:///university.db")

#bind connection when main is run
Session = sessionmaker(bind=engine)
session = Session()


# creating the tables 
Base.metadata.create_all(engine) 

# student1=Student(name='Branden',unit='Computer Science')
# Lecturer1=Lecturer(name='John',department='Engineering')


#create objects and call methods
studentName='Branden'
lecturerName='John'
# unit1=Unit('Computer Science')
unitTitle='Computer Science'
unitTitle2='Algorithms'

# student2=Student(name='Thomas',unit='Accounts')
# Lecturer2=Lecturer(name='Clarkson',department='Accounting')

studentName2='Thomas'
lecturerName2='Clarkson'


# #add objects to session
# session.add_all([student1,student2,lecturer1,unit1,unit2])
# #commit changes //after every operation commit changes
# session.commit()

# validate / assumpation handling 
# object creation / record insert to the db table 
student1=session.query(Student).filter_by(name=studentName).first()
if not student1:
    student1 = Student(name=studentName)


student2=session.query(Student).filter_by(name=studentName2).first()
if not student1:
    student2 = Student(name=studentName2)


lecturer1=session.query(Lecturer).filter_by(name=lecturerName).first()
if not lecturer1:
    lecturer1 = Lecturer(name=lecturerName)


lecturer2=session.query(Lecturer).filter_by(name=lecturerName2).first()
if not lecturer2:
    lecturer2 = Lecturer(name=lecturerName2)

unit1=session.query(Unit).filter_by(title=unitTitle).first()
if not unit1:
    unit1 = Unit(title=unitTitle)

unit2=session.query(Unit).filter_by(title=unitTitle2).first()
if not unit2:
    unit2 = Unit(title=unitTitle2)

#helper methods
lecturer1.write_unit(unit1)
student1.add_unit(unit1)
student2.add_unit(unit2)

#adding objects to session
if student1 not in session:
    session.add(student1)

if lecturer1 not in session:
    session.add(lecturer1)

if unit1 not in session:
    session.add(unit1)

if student2 not in session:
    session.add(student2)

if lecturer2 not in session:
    session.add(lecturer2)

if unit2 not in session:
    session.add(unit2)

# #commit changes //after every operation commit changes
session.commit()

# Crud  OPERATIONS
#Read
all_students=session.query(Student).all()
for student in all_students:
    print("Student name:",student.name)
    for unit in student.units:
        print("Unit",unit.title)
#Update
studenttoUpdate=session.query(Student).filter_by(name=student2).first()
if studenttoUpdate:
    studenttoUpdate.name='Ian'
    session.commit()

#Delete Data
# studenttoDelete=session.query(Student).filter_by(name="Moses").first()
# if studenttoDelete:
#     session.delete(studenttoDelete)
#     session.commit()
# else:
#     print("Author not found,unable to delete")
#close the session
session.close()


