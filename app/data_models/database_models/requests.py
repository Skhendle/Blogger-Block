from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from . import Base


class Requests(Base):
	__tablename__ = 'requests'

	by_id= Column(Integer(), primary_key = True) #id of user requesting
	for_id = Column(Integer(), ForeignKey("users.id"), primary_key = True ) #id of user being requested

	def __repr__(self):
		return f"Requests('{self.by_id}','{self.friends}')"
