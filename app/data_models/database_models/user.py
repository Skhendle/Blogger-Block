from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from . import Base



class User(Base):
	__tablename__ = 'users'
	id = Column(Integer(),primary_key = True) #db.column(type,primary key/foreign key etc)
	name = Column(String(40), unique=True)
	password = Column(String(20))
	age = Column(String(3))
	gender = Column(String(20))

	#let's establish a one-to-many relationship: one user (parent) can have many friends (children)
	# Returns a list of rows from request model, that contains id of
	# current user in the for_id column.

	friends = relationship("Requests", backref = backref("friends") ) 
	'''creates a pseudo column called 'user' in the Friends table'''
	
	#let's establish a one-to-many relationship: one user (parent) can have many posts(children)
	posts= relationship("Post", backref = backref("post_by"))
	#backref creates the opposite relationship in the other table : many-to-one

	def __repr__(self):
		return "User('{self.name}','{self.id}')".format(self)