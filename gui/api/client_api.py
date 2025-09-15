"""
client_api.py
קובץ API מדומה (Mock) כדי שהמסכים ירוצו גם בלי חיבור ל-FastAPI אמיתי.
מאוחר יותר נחליף את זה בקריאות אמיתיות עם הספרייה requests.
"""

# --- פונקציות התחברות / רישום ---
def login_user(email: str, password: str):
    # החזרת טוקן דמו
    print(f"[Mock] Login: {email} / {password}")
    return {"access_token": "fake-token", "token_type": "bearer"}

def register_user(username: str, email: str, password: str):
    # החזרת משתמש חדש דמו
    print(f"[Mock] Register: {username}, {email}")
    return {"id": 1, "username": username, "email": email}

# --- פונקציות ספרים ---
def get_books():
    print("[Mock] Fetch all books")
    return [
        {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "category": "Fantasy"},
        {"id": 2, "title": "Sherlock Holmes", "author": "Arthur Conan Doyle", "category": "Detective"},
        {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    ]

def search_books(query: str):
    print(f"[Mock] Search books: {query}")
    return [b for b in get_books() if query.lower() in b["title"].lower()]

# --- פונקציות השאלות ---
def get_loans():
    print("[Mock] Fetch all loans")
    return [
        {"id": 1, "book_id": 1, "borrow_date": "2025-01-10", "status": "borrowed"},
        {"id": 2, "book_id": 2, "borrow_date": "2025-02-05", "status": "returned"},
    ]
