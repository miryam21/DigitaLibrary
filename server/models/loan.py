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
