from queries.user_queries import (
    insert_user, get_user_by_email, get_user_by_id,
    get_all_users, update_user, delete_user
)
from models.user import User, UserCreate, UserLogin, UserUpdate
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secretkey123"   # לשים ב-.env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- הצפנת סיסמה ---
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# --- JWT ---
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- CRUD ---

def register(user: UserCreate):
    existing = get_user_by_email(user.email)
    if existing:
        return None
    hashed = hash_password(user.password)
    user_id = insert_user(user.username, user.email, hashed)
    return {"id": user_id, "username": user.username, "email": user.email, "role": "user"}

def login(user: UserLogin):
    row = get_user_by_email(user.email)
    if not row:
        return None
    user_id, username, email, password_hash, role, created_at = row
    if not verify_password(user.password, password_hash):
        return None
    token = create_access_token({"sub": str(user_id), "role": role})
    return {"access_token": token, "token_type": "bearer"}

def get_users():
    rows = get_all_users()
    return [
        {"id": r[0], "username": r[1], "email": r[2], "role": r[3], "created_at": r[4]}
        for r in rows
    ]

def get_user(user_id: int):
    row = get_user_by_id(user_id)
    if not row:
        return None
    return {"id": row[0], "username": row[1], "email": row[2], "role": row[3], "created_at": row[4]}

def update_user_service(user_id: int, data: UserUpdate):
    hashed = hash_password(data.password) if data.password else None
    ok = update_user(user_id, data.username, data.email, hashed, data.role)
    return ok

def delete_user_service(user_id: int):
    return delete_user(user_id)
