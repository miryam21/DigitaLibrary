import requests

API_URL = "http://localhost:8000"  # עדכני לכתובת השרת שלך


class BookService:
    def __init__(self, token: str = None):
        self.token = token
        print("🟢 BookService initialized | token:", "set" if token else "not set")

    def _headers(self):
        """מוסיף Authorization Header אם יש טוקן"""
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get_recommended(self, limit=5):
        """ספרים מומלצים לפי דירוג"""
        print(f"📚 Fetching recommended books | limit={limit}")
        try:
            res = requests.get(
                f"{API_URL}/books/recommended",
                params={"limit": limit},
                headers=self._headers()
            )
            print(f"   ↳ Response status: {res.status_code}")
            if res.status_code == 200:
                data = res.json()
                print(f"✅ Got {len(data)} recommended books")
                return data
            else:
                print("❌ Failed: unexpected status", res.status_code)
        except Exception as e:
            print("❌ Failed to fetch recommended books:", e)
        return []

    def get_by_category(self, category, limit=5):
        """ספרים לפי קטגוריה"""
        print(f"📚 Fetching books by category | category='{category}', limit={limit}")
        try:
            res = requests.get(
                f"{API_URL}/books/category/{category}",
                params={"limit": limit},
                headers=self._headers()
            )
            print(f"   ↳ Response status: {res.status_code}")
            if res.status_code == 200:
                data = res.json()
                print(f"✅ Got {len(data)} books in {category}")
                return data
            else:
                print("❌ Failed: unexpected status", res.status_code)
        except Exception as e:
            print("❌ Failed to fetch books by category:", e)
        return []

    def get_user_books(self, user_id, limit=10):
        """ספרים שהמשתמש שאל כרגע"""
        print(f"📚 Fetching user books | user_id={user_id}, limit={limit}")
        try:
            res = requests.get(
                f"{API_URL}/books/user/{user_id}",
                params={"limit": limit},
                headers=self._headers()
            )
            print(f"   ↳ Response status: {res.status_code}")
            if res.status_code == 200:
                data = res.json()
                print(f"✅ Got {len(data)} books for user {user_id}")
                return data
            else:
                print("❌ Failed: unexpected status", res.status_code)
        except Exception as e:
            print("❌ Failed to fetch user books:", e)
        return []

    def search_books(self, query: str, sort_by: str):
        """חיפוש ספרים לפי מילת חיפוש"""
        print(f"🔎 Searching books | query='{query}'")
        try:
            res = requests.get(
                f"{API_URL}/books/search/",
                params={"q": query, "sortBy": sort_by},
                headers=self._headers()
            )
            print(f"   ↳ Response status: {res.status_code}")
            if res.status_code == 200:
                data = res.json()
                print(f"✅ Search returned {len(data)} books for query '{query}'")
                return data
            else:
                print("❌ Failed: unexpected status", res.status_code)
        except Exception as e:
            print("❌ Failed to search books:", e)
        return []
