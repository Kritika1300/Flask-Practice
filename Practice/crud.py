from os import name
from app import db,Puppy

#create
my_puppy = Puppy('Scooby',3)
db.session.add(my_puppy)
db.session.commit()

#read
all_puppies = Puppy.query.all() #list of all Puppy(class) objects
print(all_puppies)

#select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#filter (eg. to get puppies with name sam)
puppy_sam = Puppy.query.filter_by(name = "sam")
print(puppy_sam.all()) #prints result of filter method as per __repr__ method


