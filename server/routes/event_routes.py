from fastapi import APIRouter
from models.event import Event
from services.event_service import get_events

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=list[Event])
def list_events(limit: int = 100):
    return get_events(limit)
