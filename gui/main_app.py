import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import Qt

# מייבאים את המסכים
from GUI.screens.login_screen import LoginScreen
from GUI.screens.register_screen import RegisterScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📚 Digital Library - Auth Flow")
        self.resize(900, 600)

        # מיכל לכל המסכים
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # --- יצירת מסכים ---
        self.login_screen = LoginScreen(self.navigate_to)
        self.register_screen = RegisterScreen(self.navigate_to)

        # הוספה ל־stack
        self.stack.addWidget(self.login_screen)   # index 0
        self.stack.addWidget(self.register_screen)  # index 1

        # מתחילים במסך ההתחברות
        self.stack.setCurrentWidget(self.login_screen)

        # --- טוענים עיצוב QSS ---
        try:
            with open("GUI/styles.qss", "r", encoding="utf-8") as f:
                qss = f.read()
                print("✅ QSS loaded")
                self.setStyleSheet(qss)
        except FileNotFoundError:
            print("⚠️ styles.qss not found – running without custom styles")

        # --- רקע מתכוונן ---
        self.background_path = "GUI/photos/realistic-books-shelf-library.jpg"
        self.bg_pixmap = QPixmap(self.background_path)

    def paintEvent(self, event):
        """ציור רקע עם שליטה על מיקום התמונה"""
        painter = QPainter(self)

        if not self.bg_pixmap.isNull():
            # נמתח עם פרופורציות
            scaled = self.bg_pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            # חישוב נקודת התחלה (מרכז)
            x = (self.width() - scaled.width()) // 2
            y = (self.height() - scaled.height()) // 2

            # במסכים קטנים – מזיזים קצת שמאלה
            if self.width() < 700:
                x -= 20   # ממש טוויק קטן שמאלה

            painter.drawPixmap(x, y, scaled)
        else:
            painter.fillRect(self.rect(), QColor("#2c3e50"))

        super().paintEvent(event)

    def navigate_to(self, screen_name: str):
        """מעביר בין מסכים לפי שם"""
        if screen_name == "login":
            self.stack.setCurrentWidget(self.login_screen)
        elif screen_name == "register":
            self.stack.setCurrentWidget(self.register_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
