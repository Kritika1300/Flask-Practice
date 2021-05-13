import bcrypt
from werkzeug.security import generate_password_hash,check_password_hash

#Hashing the user password
hashed_password = generate_password_hash('mysecretpassword')
print(hashed_password)


#Checking hashpassword against other passwords
check = check_password_hash(hashed_password,'mysecretpasswor')
print(check)
