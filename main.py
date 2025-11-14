# %%
import bcrypt

def hash_password(pwd):
    # Convert the password to bytes
    password_bytes = pwd.encode('utf-8')
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8') # Convert bytes back to string for storage

def validate_password(pwd, hashed):
    # Encode both the plain password and hashed password for checking
    password_bytes = pwd.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)
 
# Example usage
password = 'Magic123'
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)

is_valid = validate_password('Magic123', hashed_password) 
print("Is Valid:", is_valid)
