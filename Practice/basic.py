from app import db,Puppy,Owner,Toy

#creating 2 puppies
scoob = Puppy('Scoob')
goofy = Puppy('Goofy')

#adding the 2 puppies to db
db.session.add_all([scoob,goofy])
db.session.commit()

#check
print(Puppy.query.all())

scoob = Puppy.query.filter_by(name = 'Scoob').first()
print(scoob)

#create Owner object 
jose = Owner('Jose',scoob.id)

#Giving scoob some toys
toy1 = Toy('Chew Toy',scoob.id)
toy2 = Toy('Ball',scoob.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

scoob = Puppy.query.filter_by(name = 'Scoob').first()
print(scoob)

scoob.report_toys()