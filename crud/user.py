from models.user import User

def create_user(user: User):
    # Logic to save the user to the database
    print(f"Saving user {user.username} to the database")
