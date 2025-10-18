from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Loan(BaseModel):
    id: Optional[int] = None
    user_id: int
    book_id: int
    borrow_date: Optional[datetime] = None
    return_date: Optional[datetime] = None
    status: Optional[str] = "borrowed"

class LoanCreate(BaseModel):
    user_email: str
    book_id: int
    borrow_date: datetime

    class Config:
        # המרת תאריך ושעה לפורמט ISO אוטומטית
        json_encoders = {
            datetime: lambda x: datetime.fromisoformat(x)
        }

class LoanUpdate(BaseModel):
    return_date: Optional[datetime] = None
    status: Optional[str] = None
