from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from services.loan_service import loan_book
from services.auth_service import _session
import os

class BookScreen(QDialog):
    def __init__(self, book):
        super().__init__()

        self.book = book
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # הצגת התמונה המקדימה
        img_path = os.path.join(os.path.dirname(__file__), "..", "photos", self.book.get("thumbnail", ""))
        pixmap = QPixmap(self.book["thumbnail"]).scaled(150, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation) if self.book["thumbnail"] else None
        img = QLabel()
        if pixmap:
            img.setPixmap(pixmap)
            img.setAlignment(Qt.AlignCenter)
        else:
            img.setText("No Image Available")
            img.setAlignment(Qt.AlignCenter)
        layout.addWidget(img)

        # כותרת הספר
        title_label = QLabel(self.book["title"])
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-top: 10px;")
        layout.addWidget(title_label)

        # מחבר הספר
        author_label = QLabel(f"by {self.book['author']}")
        author_label.setAlignment(Qt.AlignCenter)
        author_label.setStyleSheet("font-size: 14px; color: #555;")
        layout.addWidget(author_label)

        # שנה
        year_label = QLabel(f"Year: {self.book['year']}")
        year_label.setAlignment(Qt.AlignCenter)
        year_label.setStyleSheet("font-size: 12px; color: #777;")
        layout.addWidget(year_label)

        # סיכום הספר
        summary_label = QLabel(self.book['summary'])
        summary_label.setWordWrap(True)
        summary_label.setAlignment(Qt.AlignLeft)
        summary_label.setStyleSheet("font-size: 12px; margin-top: 10px; color: #333;")
        layout.addWidget(summary_label)

        # קטגוריה של הספר
        category_label = QLabel(f"Category: {self.book['category']}")
        category_label.setAlignment(Qt.AlignLeft)
        category_label.setStyleSheet("font-size: 12px; color: #333;")
        layout.addWidget(category_label)

        # דירוג הספר
        rating_label = QLabel(f"Rating: {self.book['rating']}/5")
        rating_label.setAlignment(Qt.AlignLeft)
        rating_label.setStyleSheet("font-size: 12px; color: #333; margin-top: 10px;")
        layout.addWidget(rating_label)

        # כפתור השאלת הספר
        borrow_button = QPushButton("Borrow Book")
        borrow_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 10px;")
        borrow_button.clicked.connect(self.loan_book)
        layout.addWidget(borrow_button)

        # הגדרות חלון
        self.setWindowTitle(self.book["title"])
        self.setModal(True)  # הופך את ה-dialog למודאלי כך שלא יאפשר אינטראקציה עם שאר החלון עד שלא ייסגר

        self.setLayout(layout)
        self.setFixedSize(400, 600)

    def loan_book(self):
        # כאן תוכל להוסיף את הלוגיקה של השאלת הספר
        print(f"Book '{self.book['title']}' borrowed successfully!")
        print(_session)
        loan_book(_session['user'], self.book['id'])
        self.accept()  # סוגר את ה-dialog אחרי השאלה

