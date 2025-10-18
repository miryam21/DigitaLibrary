from fastapi import APIRouter, HTTPException
from services.book_service import (
    get_books, get_book, add_book, edit_book, remove_book,
    search_books_service, fetch_recommended_books,
    fetch_books_by_category, fetch_user_books
)
from models.book import Book

router = APIRouter(prefix="/books", tags=["Books"])

# === קודם נשים את ה־routes הספציפיים יותר ===

@router.get("/search/", response_model=list[Book])
def search_books(q: str, sortBy: str):
    return search_books_service(q, sortBy)


@router.get("/recommended")
def recommended_books(limit: int = 5):
    """
    ספרים מומלצים לפי דירוג ממוצע
    """
    return fetch_recommended_books(limit)


@router.get("/category/{category}")
def books_by_category(category: str, limit: int = 5):
    """
    ספרים לפי קטגוריה
    """
    return fetch_books_by_category(category, limit)


@router.get("/user/{user_id}")
def user_books(user_id: int, limit: int = 10):
    """
    ספרים שמשויכים למשתמש (ספרים שהושאלו)
    """
    return fetch_user_books(user_id, limit)


# === רק אחר כך נשים את ה־routes הגנריים ===

@router.get("/", response_model=list[Book])
def list_books(limit: int = 100):
    """
    מחזיר את כל הספרים עד limit
    """
    return get_books(limit)


@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int):
    """
    מחזיר ספר לפי ID
    """
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=Book)
def create_book(book: Book):
    """
    יצירת ספר חדש
    """
    return add_book(book)


@router.put("/{book_id}")
def update_book(book_id: int, book: Book):
    """
    עדכון ספר קיים
    """
    success = edit_book(book_id, book)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found or not updated")
    return {"message": f"Book {book_id} updated successfully"}


@router.delete("/{book_id}")
def delete_book(book_id: int):
    """
    מחיקת ספר
    """
    success = remove_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": f"Book {book_id} deleted successfully"}
