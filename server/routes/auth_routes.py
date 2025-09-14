from fastapi import APIRouter, HTTPException
from models.user import UserCreate, UserLogin
from services.user_service import register, login  # ✅ שינוי ל-user_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register_user(user: UserCreate):
    result = register(user)
    if not result:
        raise HTTPException(status_code=400, detail="User already exists")
    return result

@router.post("/login")
def login_user(user: UserLogin):
    result = login(user)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result
