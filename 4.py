import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()
    

#fix
from werkzeug.security import generate_password_hash

def hash_password(password):
    return generate_password_hash(password)
 
 