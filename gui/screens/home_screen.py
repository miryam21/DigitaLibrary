from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class HomeScreen(QWidget):
    def __init__(self, navigate_to):
        super().__init__()
        layout = QVBoxLayout()

        title = QLabel("📚 ברוכים הבאים לספרייה הדיגיטלית")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title)

        btn_login = QPushButton("כניסה / רישום")
        btn_login.clicked.connect(lambda: navigate_to("login"))
        layout.addWidget(btn_login)

        btn_books = QPushButton("ספרים")
        btn_books.clicked.connect(lambda: navigate_to("books"))
        layout.addWidget(btn_books)

        btn_loans = QPushButton("השאלות שלי")
        btn_loans.clicked.connect(lambda: navigate_to("loans"))
        layout.addWidget(btn_loans)

        btn_charts = QPushButton("סטטיסטיקות")
        btn_charts.clicked.connect(lambda: navigate_to("charts"))
        layout.addWidget(btn_charts)

        self.setLayout(layout)
