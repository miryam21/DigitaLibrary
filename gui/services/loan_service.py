import datetime

import requests

API_URL = "http://localhost:8000/loans"  # עדכני לכתובת השרת שלך

# Session גלובלי
_session = {"token": None, "user": None}


def loan_book(user_email: int, book_id: int):
    try:
        res = requests.post(f"{API_URL}/", json={
            "user_email": user_email,
            "book_id": book_id,
            "borrow_date": datetime.datetime.now().isoformat()
        })
        if res.status_code == 200:
            data = res.json()
            return data
    except Exception as e:
        print("❌ Loans register failed:", e)
    return None
