from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

class BooksScreen(QWidget):
    def __init__(self, navigate_to):
        super().__init__()
        self.navigate_to = navigate_to
        layout = QVBoxLayout()

        title = QLabel("📖 ספרים")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("חפש ספר לפי שם/מחבר/קטגוריה")
        layout.addWidget(self.search_input)

        btn_search = QPushButton("חפש")
        btn_search.clicked.connect(self.mock_search)
        layout.addWidget(btn_search)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        btn_back = QPushButton("⬅ חזרה")
        btn_back.clicked.connect(lambda: self.navigate_to("home"))
        layout.addWidget(btn_back)

        self.setLayout(layout)

    def mock_search(self):
        # דוגמה לנתונים סטטיים (עד שנחבר ל־API)
        books = [
            {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "category": "Fantasy"},
            {"id": 2, "title": "Sherlock Holmes", "author": "Arthur Conan Doyle", "category": "Detective"}
        ]
        self.fill_table(books)

    def fill_table(self, books):
        self.table.setRowCount(len(books))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Author", "Category"])
        for i, b in enumerate(books):
            self.table.setItem(i, 0, QTableWidgetItem(str(b["id"])))
            self.table.setItem(i, 1, QTableWidgetItem(b["title"]))
            self.table.setItem(i, 2, QTableWidgetItem(b["author"]))
            self.table.setItem(i, 3, QTableWidgetItem(b["category"]))
