# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from .base import Base

# class Unit(Base):
#     __tablename__ = 'units'
#     id = Column(Integer(), primary_key=True)
#     title= Column(String())


#     def __init__(self,title):
#         self.title=title

#     def add_unitmain(self,unitmain):
#           self.unitmains.append(unitmain)



#     def __str__(self):

#             return f"Unit(id:{self.id}Name:{self.name})"