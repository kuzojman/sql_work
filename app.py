from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from data import teachers_info






app = Flask(__name__)
app.secret_key = "randomstring"
# Это создаст базу в оперативной памяти, которая очистится после завершения программы.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
####app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    about = db.Column(db.String, unique=True)
    rating = db.Column(db.String, unique=True)
    picture = db.Column(db.String, unique=True)
    price = db.Column(db.Integer, unique=True)
    goals = db.Column(db.String, unique=True)
    free =  db.Column(db.String, unique=True)
    bookings = db.relationship("Booking", back_populates='teacher')




class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    name_client = db.Column(db.String)
    phone = db.Column(db.String)
    day_in_week= db.Column(db.String)
    time_to_study = db.Column(db.String)
    teacher = db.relationship("Teacher")
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))



class Proposoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_client = db.Column(db.String)
    phone = db.Column(db.String)
    trainer = db.Column(db.String)
    radio_field_week = db.Column(db.String)

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_in_english = db.Column(db.String)
    name_in_russian = db.Column(db.String)


#db.create_all()

for i in range(len(teachers_info)):
    print((teachers_info[i])["goals"])



#number = int(input())
for i in range(len(teachers_info)):
    teacher = Teacher(name=(teachers_info[i])["name"],
                     about=(teachers_info[i])["about"],
                      rating=(teachers_info[i])["rating"],
                      picture=(teachers_info[i])["picture"],
                      price=(teachers_info[i])["price"],
                      goals=(teachers_info[i])["goals"],
                      free=(teachers_info[i])["free"])
    db.session.add(teacher)
    db.session.commit()




#teacher = Teacher(name=(teachers[1])["name"],
#                  about=(teachers[1])["about"],
 #               rating=(teachers[1])["rating"],
 #               picture=(teachers[1])["picture"],
 #                 price=(teachers[1])["price"])

#db.session.add(teacher)
#db.session.commit()

#users = Teacher.query.all()

#for user in users:
#    print(user.name+" " +user.about)



