from fastapi import APIRouter, HTTPException
from models.user import User
from crud.user import create_user
from database.connection import db

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    existing_user = db.users.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    create_user(user)
    return {"message": "User registered successfully", "username": user.username}
