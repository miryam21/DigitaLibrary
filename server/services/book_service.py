from queries.book_queries import (
    fetch_all_books, fetch_book_by_id,
    insert_book, update_book, delete_book, search_books,
    get_recommended_books, get_books_by_category, get_user_books
)
from models.book import Book
from events.event_store import save_event

from queries.book_queries import get_books_by_author


def get_books(limit: int = 100):
    rows = fetch_all_books(limit)
    return [
        Book(
            id=row[0], title=row[1], author=row[2],
            year=row[3], pages=row[4], category=row[5],
            summary=row[6], cover_url=row[7], average_rating=row[8]
        )
        for row in rows
    ]


def get_book(book_id: int):
    row = fetch_book_by_id(book_id)
    if not row:
        return None
    return Book(
        id=row[0], title=row[1], author=row[2],
        year=row[3], pages=row[4], category=row[5],
        summary=row[6], cover_url=row[7], average_rating=row[8]
    )


def add_book(book: Book):
    new_id = insert_book(
        book.title, book.author, book.year,
        book.pages, book.category, book.summary, book.cover_url, book.average_rating
    )
    book.id = new_id
    save_event("BookAdded", {"book_id": new_id})
    return book


def edit_book(book_id: int, book: Book):
    updated = update_book(
        book_id, book.title, book.author, book.year,
        book.pages, book.category, book.summary, book.cover_url, book.average_rating
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


def search_books_service(query: str, sortBy: str):
    rows = []
    if sortBy == "Book name":
        rows = search_books_service(query)
    elif sortBy == "Author":
        rows = get_books_by_author(query)
    elif rows == "Category":
        rows = get_books_by_category(query)

    return [
        Book(
            id=row[0], title=row[1], author=row[2],
            year=row[3], pages=row[4], category=row[5],
            summary=row[6], cover_url=row[7], average_rating=row[8]
        )
        for row in rows
    ]


# === שירותים חדשים ===

def fetch_recommended_books(limit: int = 5):
    rows = get_recommended_books(limit)
    return [
        {
            "id": r[0], "title": r[1], "author": r[2],
            "year": r[3], "pages": r[4], "category": r[5],
            "summary": r[6], "thumbnail": r[7] or "default.jpg",
            "rating": r[8]
        }
        for r in rows
    ]


def fetch_books_by_category(category: str, limit: int = 5):
    rows = get_books_by_category(category, limit)
    return [
        {
            "id": r[0], "title": r[1], "author": r[2],
            "year": r[3], "pages": r[4], "category": r[5],
            "summary": r[6], "thumbnail": r[7] or "default.jpg",
            "rating": r[8]
        }
        for r in rows
    ]


def fetch_user_books(user_id: int, limit: int = 10):
    rows = get_user_books(user_id, limit)
    return [
        {
            "id": r[0], "title": r[1], "author": r[2],
            "year": r[3], "pages": r[4], "category": r[5],
            "summary": r[6], "thumbnail": r[7] or "default.jpg",
            "rating": r[8]
        }
        for r in rows
    ]
