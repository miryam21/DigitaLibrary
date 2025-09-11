from DB.database import get_connection
import json
from datetime import datetime

def insert_event(event_type: str, user_id: int = None, book_id: int = None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO events (event_type, user_id, book_id, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (event_type, user_id, book_id, datetime.now())
    )
    conn.commit()
    return cursor.lastrowid

def fetch_events(limit: int = 100):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT TOP {limit} id, event_type, user_id, book_id, timestamp FROM events ORDER BY timestamp DESC"
    )
    return cursor.fetchall()
