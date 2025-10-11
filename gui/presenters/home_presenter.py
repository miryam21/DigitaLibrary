from services.book_service import BookService
from services.auth_service import logout_user, get_current_user


class HomePresenter:
    def __init__(self, view, user_data=None):
        """
        :param view: ה-View (HomeScreen)
        :param user_data: נתוני המשתמש שעוברים מה-Login (אופציונלי, אפשר גם לשאוב מ-AuthService)
        """
        self.view = view
        self.user_data = user_data or {}
        self.book_service = BookService()
        print("🟢 HomePresenter initialized | user_data:", self.user_data)

    # --- טעינת נתונים למסך ---
    def load_recommended_books(self):
        print("📚 Loading recommended books...")
        books = self.book_service.get_recommended(limit=5)
        print(f"✅ Got {len(books)} recommended books")
        self.view.show_recommended_books(books)

    def load_categories(self):
        print("📚 Loading categories...")
        for cat in ["Technology", "Fiction", "History"]:
            books = self.book_service.get_by_category(cat, limit=3)
            print(f"   ➡️ Category {cat}: {len(books)} books")
            if books:
                self.view.show_category(cat, books)

    def load_user_books(self):
        print("📚 Loading user books...")
        # אם יש user_id מה-Login נשתמש בו, אחרת ננסה מה-Session
        user_id = self.user_data.get("id")
        if not user_id:
            user = get_current_user()
            if isinstance(user, dict):
                user_id = user.get("id")

        if user_id:
            books = self.book_service.get_user_books(user_id, limit=8)
            print(f"✅ Got {len(books)} books for user {user_id}")
            self.view.show_user_books(books)
        else:
            print("⚠️ No user_id found, skipping user books")

    # --- פעולות כפתורים ---
    def on_search(self, query: str):
        print(f"🔎 Search triggered | query='{query}'")
        if not query.strip():
            print("⚠️ Empty query, skipping search")
            return
        books = self.book_service.search_books(query)
        print(f"✅ Search returned {len(books)} books")
        self.view.show_search_results(books)

    def on_logout_clicked(self):
        print("👤 Logout clicked")
        logout_user()   # מנקה את ה-Session
        print("✅ Session cleared, navigating to login screen")
        self.view.show_login_screen()

    # --- מידע על המשתמש ---
    def get_welcome_username(self):
        """
        מחזיר את שם המשתמש המחובר כדי להציג ב-Welcome
        """
        if self.user_data and "username" in self.user_data:
            username = self.user_data["username"]
            print(f"👤 Using username from user_data: {username}")
            return username

        user = get_current_user()
        if isinstance(user, dict):
            username = user.get("username", "Reader")
            print(f"👤 Using username from session dict: {username}")
            return username

        if isinstance(user, str):
            print(f"👤 Using username from session string: {user}")
            return user

        print("⚠️ No username found, fallback=Reader")
        return "Reader"
