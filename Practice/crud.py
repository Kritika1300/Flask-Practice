from app import db,Puppy

#create
my_puppy = Puppy('Scooby',3)
db.session.add(my_puppy)
db.session.commit()

#read


