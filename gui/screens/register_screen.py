import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QHBoxLayout, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from presenters.auth_presenter import AuthPresenter


class RegisterScreen(QWidget):
    def __init__(self, navigate_to):
        super().__init__()
        self.navigate_to = navigate_to
        self.presenter = AuthPresenter()
        self.setObjectName("RegisterScreen")

        base_dir = os.path.join(os.path.dirname(__file__), "..", "icons")

        main_layout = QVBoxLayout(self)
        form_container = QFrame()
        form_container.setObjectName("FormContainer")
        form_layout = QVBoxLayout(form_container)

        title = QLabel("Start Your Reading Journey")
        title.setObjectName("RegisterTitle")
        title.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title)

        username_label = QLabel("Username")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Pick a nickname")
        self.username_input.setObjectName("RegisterInput")
        self.username_input.addAction(QIcon(os.path.join(base_dir, "user.png")), QLineEdit.LeadingPosition)

        email_label = QLabel("Email Address")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setObjectName("RegisterInput")
        self.email_input.addAction(QIcon(os.path.join(base_dir, "email.png")), QLineEdit.LeadingPosition)

        password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Create a password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setObjectName("RegisterInput")
        self.password_input.addAction(QIcon(os.path.join(base_dir, "password.png")), QLineEdit.LeadingPosition)

        confirm_label = QLabel("Confirm Password")
        self.confirm_input = QLineEdit()
        self.confirm_input.setPlaceholderText("Repeat your password")
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setObjectName("RegisterInput")
        self.confirm_input.addAction(QIcon(os.path.join(base_dir, "password.png")), QLineEdit.LeadingPosition)

        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(confirm_label)
        form_layout.addWidget(self.confirm_input)

        btn_register = QPushButton(" Join the Library")
        btn_register.setObjectName("RegisterButton")
        btn_register.setIcon(QIcon(os.path.join(base_dir, "register.png")))
        btn_register.clicked.connect(self.handle_register)
        form_layout.addWidget(btn_register)

        footer = QFrame()
        footer_layout = QHBoxLayout(footer)
        footer_layout.setAlignment(Qt.AlignCenter)

        footer_text = QLabel("Already a member?")
        footer_link = QPushButton(" Sign In")
        footer_link.setObjectName("RegisterSwitchButton")
        footer_link.setIcon(QIcon(os.path.join(base_dir, "login.png")))
        footer_link.clicked.connect(lambda: self.navigate_to("login"))

        footer_layout.addWidget(footer_text)
        footer_layout.addWidget(footer_link)

        form_layout.addWidget(footer)
        main_layout.addWidget(form_container, alignment=Qt.AlignCenter)

    def clear_fields(self):
        """מאפס את כל השדות"""
        self.username_input.clear()
        self.email_input.clear()
        self.password_input.clear()
        self.confirm_input.clear()

    def handle_register(self):
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        confirm = self.confirm_input.text()

        if password != confirm:
            QMessageBox.warning(self, "Error", "Passwords do not match")
            return

        result = self.presenter.register(username, email, password)
        if result:
            QMessageBox.information(self, "Success", "Account created! Please login.")
            self.clear_fields()
            self.navigate_to("login")
        else:
            QMessageBox.warning(self, "Error", "Registration failed. Email may already exist.")
