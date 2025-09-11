from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Event(BaseModel):
    id: Optional[int] = None
    event_type: str
    user_id: Optional[int] = None
    book_id: Optional[int] = None
    timestamp: Optional[datetime] = None
