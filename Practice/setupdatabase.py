from app import db,Puppy

#creates all tables (transforms model class to db table)
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Franky',4)

db.session.add_all([sam,frank]) #or db.session.add(sam)  db.session.add(frank)


print(sam.id)
print(frank.id)

db.session.commit() #save changes to db

print(sam.id)
print(frank.id)