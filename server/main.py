from fastapi import FastAPI
from routes.book_routes import router as book_router
from routes.event_routes import router as event_router

app = FastAPI(title="Digital Library API")

@app.get("/")
def root():
    return {"message": "📚 API is running!"}

# חיבור של כל ה־routers
app.include_router(book_router)
app.include_router(event_router)
