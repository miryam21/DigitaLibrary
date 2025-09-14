from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime
import password_validator

# ✨ סכמת סיסמאות (פשוטה יותר)
password_schema = password_validator.PasswordValidator()
password_schema \
    .min(8) \
    .max(100) \
    .has().letters() \
    .has().digits()

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    role: Optional[str] = "user"
    created_at: Optional[datetime] = None

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, v: str):
        if not password_schema.validate(v):
            raise ValueError(
                "Password must be at least 8 characters long and contain both letters and numbers"
            )
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    password: Optional[str] = None

    @field_validator("password")
    def validate_password(cls, v: Optional[str]):
        if v is None:
            return v
        if not password_schema.validate(v):
            raise ValueError(
                "Password must be at least 8 characters long and contain both letters and numbers"
            )
        return v
