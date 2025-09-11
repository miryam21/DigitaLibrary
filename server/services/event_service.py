from queries.event_queries import insert_event, fetch_events
from models.event import Event

def save_event(event_type: str, user_id: int = None, book_id: int = None):
    event_id = insert_event(event_type, user_id, book_id)
    return {"id": event_id, "event_type": event_type, "user_id": user_id, "book_id": book_id}

def get_events(limit: int = 100):
    rows = fetch_events(limit)
    return [
        Event(
            id=row.id,
            event_type=row.event_type,
            user_id=row.user_id,
            book_id=row.book_id,
            timestamp=row.timestamp
        )
        for row in rows
    ]
