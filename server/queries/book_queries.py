from DB.database import get_connection


def fetch_all_books(limit: int = 100):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT TOP {limit} 
            id, title, author, year, pages, category, summary, cover_url, average_rating
        FROM books
        ORDER BY id
        """
    )
    return cursor.fetchall()


def fetch_book_by_id(book_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, title, author, year, pages, category, summary, cover_url, average_rating
        FROM books
        WHERE id = ?
        """,
        (book_id,)
    )
    return cursor.fetchone()


def insert_book(title, author, year, pages, category, summary, cover_url, average_rating=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, year, pages, category, summary, cover_url, average_rating)
        OUTPUT INSERTED.id
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (title, author, year, pages, category, summary, cover_url, average_rating))

    new_id = cursor.fetchone()[0]
    conn.commit()
    return new_id


def update_book(book_id, title, author, year, pages, category, summary, cover_url, average_rating=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books
        SET title=?, author=?, year=?, pages=?, category=?, summary=?, cover_url=?, average_rating=?
        WHERE id=?
    """, (title, author, year, pages, category, summary, cover_url, average_rating, book_id))
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
        SELECT id, title, author, year, pages, category, summary, cover_url, average_rating
        FROM books
        WHERE title LIKE ? OR author LIKE ? OR category LIKE ?
    """, (like, like, like))
    return cursor.fetchall()


# === פונקציות חדשות ===

def get_recommended_books(limit: int = 5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT TOP {limit} id, title, author, year, pages, category, summary, cover_url, average_rating
        FROM books
        WHERE average_rating IS NOT NULL
        ORDER BY average_rating DESC
    """)
    return cursor.fetchall()


def get_books_by_category(category: str, limit: int = 5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT TOP {limit} id, title, author, year, pages, category, summary, cover_url, average_rating
        FROM books
        WHERE category = ?
    """, (category,))
    return cursor.fetchall()


def get_user_books(user_id: int, limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT TOP {limit} 
            b.id, b.title, b.author, b.year, b.pages, b.category, b.summary, b.cover_url, b.average_rating
        FROM loans l
        JOIN books b ON l.book_id = b.id
        WHERE l.user_id = ? AND l.status = 'borrowed'
    """, (user_id,))
    return cursor.fetchall()
