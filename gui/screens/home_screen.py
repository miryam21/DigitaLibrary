import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QFrame, QGridLayout, QTabWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon

# 👇 חיבור ל-Presenter
from presenters.home_presenter import HomePresenter


class HomeScreen(QWidget):
    def __init__(self, user_data, navigate_to):
        """
        :param user_data: המידע על המשתמש שהתחבר
        :param navigate_to: פונקציית ניווט מ-MainWindow (כדי שנוכל לחזור ל-login)
        """
        super().__init__()
        self.user_data = user_data
        self.navigate_to = navigate_to
        self.setObjectName("HomeScreen")

        # === Presenter ===
        self.presenter = HomePresenter(self, user_data)

        base_dir = os.path.join(os.path.dirname(__file__), "..", "icons")

        # === Layout ראשי ===
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # === Topbar ===
        topbar = QHBoxLayout()
        username = self.presenter.get_welcome_username()
        welcome = QLabel(f"Welcome, {username} ")
        welcome.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search for a book...")
        self.search_input.setFixedHeight(32)
        self.search_input.addAction(QIcon(os.path.join(base_dir, "search.png")), QLineEdit.LeadingPosition)

        btn_search = QPushButton(" Search")
        btn_search.setFixedHeight(32)
        btn_search.setIcon(QIcon(os.path.join(base_dir, "search.png")))
        btn_search.clicked.connect(lambda: self.presenter.on_search(self.search_input.text()))

        btn_logout = QPushButton(" Logout")
        btn_logout.setFixedHeight(32)
        btn_logout.setIcon(QIcon(os.path.join(base_dir, "logout.png")))
        btn_logout.clicked.connect(self.presenter.on_logout_clicked)  # 👈 חיבור ל-Presenter

        topbar.addWidget(welcome)
        topbar.addStretch()
        topbar.addWidget(self.search_input)
        topbar.addWidget(btn_search)
        topbar.addWidget(btn_logout)

        main_layout.addLayout(topbar)

        # === Tabs ===
        self.tabs = QTabWidget()
        self.tabs.setObjectName("HomeTabs")
        main_layout.addWidget(self.tabs)

        # --- Tab 1: Library ---
        library_tab = QWidget()
        lib_layout = QVBoxLayout(library_tab)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        self.content_layout = QVBoxLayout(content)
        self.content_layout.setSpacing(30)
        scroll.setWidget(content)
        lib_layout.addWidget(scroll)

        self.tabs.addTab(library_tab, " Library")

        # --- Tab 2: Statistics ---
        stats_tab = QWidget()
        stats_layout = QVBoxLayout(stats_tab)

        lbl_stats = QLabel(" Here we'll show statistics (graphs) about books")
        lbl_stats.setAlignment(Qt.AlignCenter)
        lbl_stats.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50;")

        stats_layout.addWidget(lbl_stats)
        self.tabs.addTab(stats_tab, " Statistics")

        # --- Tab 3: My Books ---
        my_books_tab = QWidget()
        self.my_books_layout = QVBoxLayout(my_books_tab)

        lbl_mybooks = QLabel(" These are the books you borrowed")
        lbl_mybooks.setAlignment(Qt.AlignCenter)
        lbl_mybooks.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50;")
        self.my_books_layout.addWidget(lbl_mybooks)

        self.tabs.addTab(my_books_tab, " My Books")

        # === קריאה לנתונים דרך ה-Presenter ===
        self.presenter.load_recommended_books()
        self.presenter.load_categories()
        self.presenter.load_user_books()

    # === פונקציות שה-Presenter קורא ===
    def show_recommended_books(self, books):
        self.add_section("⭐ Recommended Books", books, limit=5)

    def show_category(self, category, books):
        self.add_section(category, books, limit=3, show_more=True)

    def show_user_books(self, books):
        grid_container = QWidget()
        grid = QGridLayout(grid_container)
        grid.setSpacing(15)

        for i, book in enumerate(books):
            card = self.create_book_card(book)
            row, col = divmod(i, 4)
            grid.addWidget(card, row, col)

        self.my_books_layout.addWidget(grid_container)

    def show_search_results(self, books):
        self.add_section("🔎 Search Results", books, limit=10)

    def show_login_screen(self):
        """כאן חוזרים למסך login דרך MainWindow"""
        self.navigate_to("login")

    def add_section(self, title, books, limit=5, show_more=False):
        """יוצר סקשן עם כותרת וכרטיסי ספרים"""
        section = QVBoxLayout()

        header = QHBoxLayout()
        lbl = QLabel(title)
        lbl.setProperty("sectionTitle", True)
        header.addWidget(lbl)
        header.addStretch()

        if show_more:
            btn_more = QPushButton("See More")
            btn_more.setFixedHeight(28)
            btn_more.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "..", "icons", "arrow-right.png")))
            btn_more.setObjectName("SeeMoreButton")
            header.addWidget(btn_more)

        section.addLayout(header)

        grid_container = QWidget()
        grid = QGridLayout(grid_container)
        grid.setSpacing(15)

        for i, book in enumerate(books[:limit]):
            card = self.create_book_card(book)
            row, col = divmod(i, 4)
            grid.addWidget(card, row, col)

        section.addWidget(grid_container)
        self.content_layout.addLayout(section)

    def create_book_card(self, book):
        """יוצר כרטיס ספר יחיד"""
        card = QFrame()
        card.setObjectName("BookCard")
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignTop)

        img_path = os.path.join(os.path.dirname(__file__), "..", "photos", book.get("thumbnail", ""))
        if os.path.exists(img_path):
            pixmap = QPixmap(img_path).scaled(120, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            img = QLabel()
            img.setPixmap(pixmap)
            img.setAlignment(Qt.AlignCenter)
            layout.addWidget(img)

        title = QLabel(book["title"])
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)

        author = QLabel(f"by {book['author']}")
        author.setAlignment(Qt.AlignCenter)
        author.setStyleSheet("font-size: 12px; color: #555;")
        layout.addWidget(author)

        btn_details = QPushButton(" Details")
        btn_details.setFixedHeight(28)
        btn_details.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "..", "icons", "info.png")))
        layout.addWidget(btn_details)

        return card
