from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    role: Optional[str] = "user"
