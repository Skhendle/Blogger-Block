from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from . import Base



class User(Base):

	__tablename__ = 'users'

	id = Column(Integer, primary_key = True, nullable = False)
	username = Column(String(40), nullable = False, unique=True)
	password = Column(String(20),nullable = False)
	age = Column(Integer())
	gender = Column(String(20), default=None)

	def __repr__(self):
		# Tesing the use of format in classes
		return "User({self.username},{self.gender}), {self.posts}".format(self=self)
