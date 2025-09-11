from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None   # לא שולחים ב־POST, נוצר אוטומטית
    title: str
    author: Optional[str] = None
    year: Optional[int] = None
    pages: Optional[int] = None
    category: Optional[str] = None
    summary: Optional[str] = None
    cover_url: Optional[str] = None
