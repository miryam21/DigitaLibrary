from fastapi import APIRouter, HTTPException
from services.book_service import (
    get_books, get_book, add_book, edit_book, remove_book
)
from models.book import Book

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[Book])
def list_books(limit: int = 100):
    return get_books(limit)

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=Book)
def create_book(book: Book):
    return add_book(book)

@router.put("/{book_id}")
def update_book(book_id: int, book: Book):
    data = book.dict(exclude_unset=True)  # יתעלם מ-id אם המשתמש לא שלח
    success = edit_book(book_id, Book(**data))
    ...

@router.delete("/{book_id}")
def delete_book(book_id: int):
    success = remove_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": f"Book {book_id} deleted successfully"}
