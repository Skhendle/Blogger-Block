from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


from datetime import datetime
from . import Base


class Post(Base):

	__tablename__ = 'posts'
	id = Column(Integer,primary_key = True, unique = True)
	user_id = Column(Integer, ForeignKey("users.id"), nullable = False)	#referenceces user(Id)
	heading = Column(String(100))
	body= Column(String(200))
	date = Column(DateTime(), default=datetime.now)
	
	# link a post to a user
	# relationship is a one to many : one user many post, 
	user = relationship("User", backref=backref('posts', order_by=id))

	def __repr__(self):
		return f"Post('{self.heading}','{self.body}')"