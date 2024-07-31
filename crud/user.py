from models.user import User
from database.connection import db
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def create_user(user: User):
    hashed_password = hash_password(user.password)
    user_data = {
        "username": user.username,
        "password": hashed_password
    }
    db.users.insert_one(user_data)
    print(f"User {user.username} saved to the database")
