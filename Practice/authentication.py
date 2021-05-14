import bcrypt
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'mysecretpassword'

#Hashing the user password
hashed_password = bcrypt.generate_password_hash(password=password)
print(hashed_password)


#Checking hashpassword against other passwords
check = bcrypt.check_password_hash(hashed_password,'mysecretpassword')
print(check)
