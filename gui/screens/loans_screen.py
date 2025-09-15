from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

class LoansScreen(QWidget):
    def __init__(self, navigate_to):
        super().__init__()
        self.navigate_to = navigate_to
        layout = QVBoxLayout()

        title = QLabel("📚 ההשאלות שלי")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        btn_refresh = QPushButton("רענן")
        btn_refresh.clicked.connect(self.mock_loans)
        layout.addWidget(btn_refresh)

        btn_back = QPushButton("⬅ חזרה")
        btn_back.clicked.connect(lambda: self.navigate_to("home"))
        layout.addWidget(btn_back)

        self.setLayout(layout)

    def mock_loans(self):
        # דוגמה לנתונים סטטיים (עד שנחבר ל־API)
        loans = [
            {"id": 1, "book_id": 1, "borrow_date": "2025-01-10", "status": "borrowed"},
            {"id": 2, "book_id": 2, "borrow_date": "2025-02-05", "status": "returned"}
        ]
        self.table.setRowCount(len(loans))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Book ID", "Borrow Date", "Status"])
        for i, l in enumerate(loans):
            self.table.setItem(i, 0, QTableWidgetItem(str(l["id"])))
            self.table.setItem(i, 1, QTableWidgetItem(str(l["book_id"])))
            self.table.setItem(i, 2, QTableWidgetItem(l["borrow_date"]))
            self.table.setItem(i, 3, QTableWidgetItem(l["status"]))
