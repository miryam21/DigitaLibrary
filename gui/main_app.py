import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import Qt

from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen
from screens.home_screen import HomeScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📚 Digital Library")
        self.resize(900, 600)

        # 🔑 המשתמש המחובר
        self.current_user = None
        self.home_screen = None

        def set_user(user_data):
            self.current_user = user_data
            print("🔑 Logged in user:", user_data)

        # Stack למסכים
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # --- יצירת מסכים ---
        self.login_screen = LoginScreen(self.navigate_to, set_user)
        self.register_screen = RegisterScreen(self.navigate_to)

        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.register_screen)

        # מסך התחלתי
        self.stack.setCurrentWidget(self.login_screen)

        # --- טעינת QSS ---
        self.load_styles()

        # --- רקע מתכוונן ---
        self.background_path = os.path.join(
            os.path.dirname(__file__),
            "photos",
            "realistic-books-shelf-library.jpg"
        )
        self.bg_pixmap = QPixmap(self.background_path)

    def load_styles(self):
        """טוען את כל קבצי ה־QSS"""
        styles_dir = os.path.join(os.path.dirname(__file__), "styles")
        qss_files = ["common.qss", "auth.qss", "home.qss"]

        full_style = ""
        for qss_file in qss_files:
            path = os.path.join(styles_dir, qss_file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    full_style += f.read() + "\n"
            except FileNotFoundError:
                print(f"⚠️ {qss_file} not found")

        self.setStyleSheet(full_style)

    def paintEvent(self, event):
        """ציור רקע עם שליטה על מיקום"""
        painter = QPainter(self)

        if not self.bg_pixmap.isNull():
            scaled = self.bg_pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            # ברירת מחדל – במרכז
            x = (self.width() - scaled.width()) // 2
            y = (self.height() - scaled.height()) // 2

            # 📌 במסכים בינוניים – הזזה קלה ימינה
            if 700 < self.width() < 1200:
                x += 40

            painter.drawPixmap(x, y, scaled)
        else:
            painter.fillRect(self.rect(), QColor("#2c3e50"))

        super().paintEvent(event)

    def navigate_to(self, screen_name: str):
        """מעביר בין מסכים לפי שם וגם מאפס שדות"""
        if screen_name == "login":
            self.login_screen.clear_fields()
            self.stack.setCurrentWidget(self.login_screen)
            print("🔄 Switched to LOGIN")

        elif screen_name == "register":
            self.register_screen.clear_fields()
            self.stack.setCurrentWidget(self.register_screen)
            print("🔄 Switched to REGISTER")

        elif screen_name == "home":
            if self.current_user is None:
                print("⚠️ No user logged in – redirecting to login")
                self.stack.setCurrentWidget(self.login_screen)
                return

            # 🗑️ תמיד נבנה HomeScreen חדש עם המשתמש הנוכחי
            if self.home_screen is not None:
                self.stack.removeWidget(self.home_screen)
                self.home_screen.deleteLater()
                self.home_screen = None

            self.home_screen = HomeScreen(self.current_user, self.navigate_to)
            self.stack.addWidget(self.home_screen)
            self.stack.setCurrentWidget(self.home_screen)
            print(f"➡️ Switched to HOME (user: {self.current_user.get('username')})")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
