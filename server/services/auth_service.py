from queries.user_queries import insert_user, get_user_by_email
from models.user import UserCreate, UserLogin
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

# === הגדרות בסיסיות ===
SECRET_KEY = "secretkey123"   # 🔒 שימי בקובץ .env בעתיד
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# === פונקציות עזר ===

def hash_password(password: str):
    """הצפנת סיסמה"""
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """בדיקת סיסמה מול ההאש"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """יצירת JWT Token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# === שירותי משתמשים ===

def register(user: UserCreate):
    """רישום משתמש חדש"""
    existing = get_user_by_email(user.email)
    if existing:
        return None  # כבר קיים

    hashed = hash_password(user.password)
    user_id = insert_user(user.username, user.email, hashed)

    return {
        "id": user_id,
        "username": user.username,
        "email": user.email,
        "role": "user"
    }


def login(user: UserLogin):
    """התחברות משתמש קיים"""
    row = get_user_by_email(user.email)
    if not row:
        return None

    user_id, username, email, password_hash, role, created_at = row

    if not verify_password(user.password, password_hash):
        return None

    token = create_access_token({"sub": str(user_id), "role": role})

    # 👇 החזרת פרטי משתמש מלאים + טוקן
    return {
        "access_token": token,
        "token_type": "bearer",
        "id": user_id,
        "username": username,
        "email": email,
        "role": role
    }


def get_current_user(token: str):
    """שליפת המשתמש מתוך ה־JWT"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            return None

        row = get_user_by_email_by_id(int(user_id))  # צריך פונקציה ב-queries לפי id
        if not row:
            return None

        user_id, username, email, password_hash, role, created_at = row
        return {"id": user_id, "username": username, "email": email, "role": role}

    except JWTError:
        return None



