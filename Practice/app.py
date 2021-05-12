import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

#creating sqlite db purely through python

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Puppy(db.Model):
    #manually setting the tablename

    __tablename__ = 'puppies'

    #adding columns to the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Puppy {self.name} is {self.age} years old !'
        

app.run(port = 5000,debug= True)

