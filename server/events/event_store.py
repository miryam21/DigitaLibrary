from DB.database import get_connection
from datetime import datetime

# 📌 שמירת אירוע חדש בטבלת events
def save_event(event_type: str, payload: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO events (event_type, user_id, book_id, timestamp)
        OUTPUT INSERTED.id
        VALUES (?, ?, ?, ?)
        """,
        (
            event_type,
            payload.get("user_id"),
            payload.get("book_id"),
            datetime.now()
        )
    )
    new_id = cursor.fetchone()[0]  # לוקחים את ה-id החדש מהשורה שנכנסה
    conn.commit()
    return new_id

# 📌 שליפת אירועים קיימים
def get_events(limit: int = 100):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT TOP {limit} id, event_type, user_id, book_id, timestamp FROM events ORDER BY timestamp DESC"
    )
    rows = cursor.fetchall()

    events = []
    for row in rows:
        events.append({
            "id": row.id,
            "event_type": row.event_type,
            "user_id": row.user_id,
            "book_id": row.book_id,
            "timestamp": row.timestamp
        })
    return events
