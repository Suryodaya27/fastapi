from fastapi import APIRouter, HTTPException
from models.user import User
from crud.user import create_user

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    # convert password to hash
    # idhar password ko hash me convert kar and db me save kar
    
    create_user(user)
    return {"message": "User registered successfully", "username": user.username}
