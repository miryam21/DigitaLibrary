from queries.book_queries import (
    fetch_all_books, fetch_book_by_id,
    insert_book, update_book, delete_book, search_books
)
from models.book import Book
from events.event_store import save_event

def get_books(limit: int = 100):
    rows = fetch_all_books(limit)
    return [
        Book(
            id=row[0],
            title=row[1],
            author=row[2],
            year=row[3],
            pages=row[4],
            category=row[5],
            summary=row[6],
            cover_url=row[7]
        )
        for row in rows
    ]

def get_book(book_id: int):
    row = fetch_book_by_id(book_id)
    if not row:
        return None
    return Book(
        id=row[0],
        title=row[1],
        author=row[2],
        year=row[3],
        pages=row[4],
        category=row[5],
        summary=row[6],
        cover_url=row[7]
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

def search_books_service(query: str):
    rows = search_books(query)
    return [
        Book(
            id=row[0],
            title=row[1],
            author=row[2],
            year=row[3],
            pages=row[4],
            category=row[5],
            summary=row[6],
            cover_url=row[7]
        )
        for row in rows
    ]
