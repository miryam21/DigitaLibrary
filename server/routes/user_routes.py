from fastapi import APIRouter, HTTPException
from models.user import UserCreate, UserLogin, UserUpdate
from services.user_service import (
    register, login, get_users, get_user,
    update_user_service, delete_user_service
)

router = APIRouter(prefix="/users", tags=["Users"])

# --- יצירת יוזר (Register) ---
@router.post("/register")
def register_user(user: UserCreate):
    result = register(user)
    if not result:
        raise HTTPException(status_code=400, detail="User already exists")
    return result

# --- התחברות ---
@router.post("/login")
def login_user(user: UserLogin):
    result = login(user)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result

# --- כל המשתמשים ---
@router.get("/")
def list_users():
    return get_users()

# --- משתמש לפי ID ---
@router.get("/{user_id}")
def read_user(user_id: int):
    result = get_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

# --- עדכון משתמש ---
@router.put("/{user_id}")
def update_user_route(user_id: int, data: UserUpdate):
    ok = update_user_service(user_id, data)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found or no changes")
    return {"success": True}

# --- מחיקת משתמש ---
@router.delete("/{user_id}")
def delete_user_route(user_id: int):
    ok = delete_user_service(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True}
