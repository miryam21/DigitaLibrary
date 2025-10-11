import requests

API_URL = "http://localhost:8000"  # עדכני לכתובת השרת שלך

# Session גלובלי
_session = {"token": None, "user": None}


def login_user(email: str, password: str):
    try:
        res = requests.post(f"{API_URL}/auth/login", json={
            "email": email,
            "password": password
        })
        if res.status_code == 200:
            data = res.json()
            _session["token"] = data.get("access_token")
            _session["user"] = data.get("user") or email
            return data
    except Exception as e:
        print("❌ Login request failed:", e)
    return None


def register_user(username: str, email: str, password: str):
    try:
        res = requests.post(f"{API_URL}/auth/register", json={
            "username": username,
            "email": email,
            "password": password
        })
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print("❌ Register request failed:", e)
    return None


def logout_user():
    """ניקוי session"""
    print("👋 Logged out")
    _session["token"] = None
    _session["user"] = None


def get_token():
    return _session["token"]


def get_current_user():
    return _session["user"]
