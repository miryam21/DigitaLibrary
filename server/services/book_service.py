from queries.book_queries import (
    fetch_all_books, fetch_book_by_id,
    insert_book, update_book, delete_book
)
from models.book import Book
from events.event_store import save_event

def get_books(limit: int = 100):
    rows = fetch_all_books(limit)
    return [
        Book(
            id=row.id,
            title=row.title,
            author=row.author,
            year=row.year,
            pages=row.pages,
            category=row.category,
            summary=row.summary,
            cover_url=row.cover_url
        )
        for row in rows
    ]

def get_book(book_id: int):
    row = fetch_book_by_id(book_id)
    if not row:
        return None
    return Book(
        id=row.id,
        title=row.title,
        author=row.author,
        year=row.year,
        pages=row.pages,
        category=row.category,
        summary=row.summary,
        cover_url=row.cover_url
    )

def add_book(book: Book):
    new_id = insert_book(
        book.title, book.author, book.year,
        book.pages, book.category, book.summary, book.cover_url
    )
    book.id = new_id
    save_event("BookAdded", {"book_id": new_id})
    return book

def edit_book(book_id: int, book: Book):
    updated = update_book(
        book_id, book.title, book.author, book.year,
        book.pages, book.category, book.summary, book.cover_url
    )
    if updated:
        save_event("BookUpdated", {"book_id": book_id})
        return True
    return False

def remove_book(book_id: int):
    deleted = delete_book(book_id)
    if deleted:
        save_event("BookDeleted", {"book_id": book_id})
        return True
    return False
