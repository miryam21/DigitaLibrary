from DB.database import get_connection

def fetch_all_books(limit: int = 100):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT TOP {limit} id, title, author, year, pages, category, summary, cover_url FROM books ORDER BY id"
    )
    return cursor.fetchall()

def fetch_book_by_id(book_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, author, year, pages, category, summary, cover_url FROM books WHERE id = ?",
        (book_id,)
    )
    return cursor.fetchone()

def insert_book(title, author, year, pages, category, summary, cover_url):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, year, pages, category, summary, cover_url)
        OUTPUT INSERTED.id
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (title, author, year, pages, category, summary, cover_url))

    new_id = cursor.fetchone()[0]
    conn.commit()
    return new_id

def update_book(book_id, title, author, year, pages, category, summary, cover_url):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books
        SET title=?, author=?, year=?, pages=?, category=?, summary=?, cover_url=?
        WHERE id=?
    """, (title, author, year, pages, category, summary, cover_url, book_id))
    conn.commit()
    return cursor.rowcount

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    return cursor.rowcount

def search_books(query: str):
    conn = get_connection()
    cursor = conn.cursor()
    like = f"%{query}%"
    cursor.execute("""
        SELECT id, title, author, year, pages, category, summary, cover_url
        FROM books
        WHERE title LIKE ? OR author LIKE ? OR category LIKE ?
    """, (like, like, like))
    return cursor.fetchall()
