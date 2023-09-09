# for one to one or one to many or manny to many rships
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///university.db')
Session = sessionmaker(bind=engine)
session = Session()


