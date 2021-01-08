from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = #sqlite:////home/mbongiseni/Documents/induna/graph_sql.db'

db = SQLAlchemy(app) # create a database instance

# we can use classes/models to represent our database structure
#each class is going to be it's own table in the database. That is, class = table of database


#1.let's create the user table
class User(db.Model):
	id = db.Column(db.Integer,primary_key = True,nullable = False) #db.column(type,primary key/foreign key etc)
	name = db.Column(db.String(40),nullable = False)
	password = db.Column(db.String(20),nullable = False)
	age = db.Column(db.String(3))
	gender = db.Column(db.String(20))

	def __repr__(self):
		return f"User('{self.name}','{self.gender}')"	


class Post(db.Model):
	Id = db.Column(db.Integer,primary_key = True, unique = True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable = False)#referenceces user(Id)
	heading = db.Column(db.String(200))
	body= db.Column(db.String(100)) 
	
	def __repr__(self):
		return f"Post('{self.heading}','{self.body}')"

##############################################
#some commends
###############################

def main():

	db.create_all()
#from sqlalc import db
#from sqlalc import User,Post
#user_1 = User(id = 12,name ='mbo',password = 'word',age = '12',gender = 'male')
#post_1 = Post(Id = 23,user_id = 14,heading = 'come to god',body = 'now')
#db.session.add(user_1)
#db.session.commit()
#User.query.all()

if __name__  == "__main__":
	main()
