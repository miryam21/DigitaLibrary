from fastapi import FastAPI
from routes.book_routes import router as book_router
from routes.event_routes import router as event_router
from routes.auth_routes import router as auth_router
from routes.user_routes import router as user_router   # ✅ הוספנו
from routes.loan_routes import router as loan_router

app = FastAPI(title="Digital Library API")

@app.get("/")
def root():
    return {"message": "📚 API is running!"}

# --- חיבור ה־routers ---
app.include_router(book_router)
app.include_router(event_router)
app.include_router(auth_router)
app.include_router(user_router)   # ✅ הוספנו
app.include_router(loan_router)
