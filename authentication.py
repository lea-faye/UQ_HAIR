import hashlib
import os


# Setting a password
def set_password(users_password):
    byte_password = users_password.encode()
    hashed_password = hashlib.sha256(byte_password)
    login_hash = hashed_password.hexdigest()
    with open("login.txt", "w") as f:
        f.write(login_hash)
    
# Checking if password is correct
def check_password(attempt):
    byte_attempt = attempt.encode()
    hashed_attempt = hashlib.sha256(byte_attempt)
    login_attempt = hashed_attempt.hexdigest()
    with open("login.txt", "r") as f:
        correct_hash = f.read()
    return login_attempt == correct_hash

def authenticate():
    if os.path.exists("login.txt"):
        login = check_password(input("Enter your password: "))
        return login
    else:
        set_password(input("Enter a password: "))
        return True
