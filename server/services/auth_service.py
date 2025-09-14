from queries.user_queries import insert_user, get_user_by_email
from models.user import UserCreate, UserLogin
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secretkey123"   # 🔒 מומלץ לשים ב-.env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# הצפנת סיסמה
def hash_password(password: str):
    return pwd_context.hash(password)

# בדיקת סיסמה
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# יצירת JWT
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 📌 הרשמה
def register(user: UserCreate):
    existing = get_user_by_email(user.email)
    if existing:
        return None  # כבר קיים
    hashed = hash_password(user.password)
    user_id = insert_user(user.username, user.email, hashed)
    return {"id": user_id, "username": user.username, "email": user.email, "role": "user"}

# 📌 התחברות
def login(user: UserLogin):
    row = get_user_by_email(user.email)
    if not row:
        return None
    user_id, username, email, password_hash, role, created_at = row
    if not verify_password(user.password, password_hash):
        return None
    token = create_access_token({"sub": str(user_id), "role": role})
    return {"access_token": token, "token_type": "bearer"}
