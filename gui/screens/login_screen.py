import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QHBoxLayout, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from presenters.auth_presenter import AuthPresenter


class LoginScreen(QWidget):
    def __init__(self, navigate_to, set_user):
        super().__init__()
        self.navigate_to = navigate_to
        self.set_user = set_user
        self.presenter = AuthPresenter()
        self.setObjectName("LoginScreen")

        base_dir = os.path.join(os.path.dirname(__file__), "..", "icons")

        main_layout = QVBoxLayout(self)
        form_container = QFrame()
        form_container.setObjectName("FormContainer")
        form_layout = QVBoxLayout(form_container)

        title = QLabel("Start your reading..")
        title.setObjectName("LoginTitle")
        title.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title)

        email_label = QLabel("Email Address")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setObjectName("LoginInput")
        self.email_input.addAction(QIcon(os.path.join(base_dir, "email.png")), QLineEdit.LeadingPosition)

        password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setObjectName("LoginInput")
        self.password_input.addAction(QIcon(os.path.join(base_dir, "password.png")), QLineEdit.LeadingPosition)

        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)

        btn_login = QPushButton(" Sign In")
        btn_login.setObjectName("LoginButton")
        btn_login.setIcon(QIcon(os.path.join(base_dir, "login.png")))
        btn_login.clicked.connect(self.handle_login)
        form_layout.addWidget(btn_login)

        footer = QFrame()
        footer_layout = QHBoxLayout(footer)
        footer_layout.setAlignment(Qt.AlignCenter)

        footer_text = QLabel("New here?")
        footer_link = QPushButton(" Create your Library Card")
        footer_link.setObjectName("LoginSwitchButton")
        footer_link.setIcon(QIcon(os.path.join(base_dir, "register.png")))
        footer_link.clicked.connect(lambda: self.navigate_to("register"))

        footer_layout.addWidget(footer_text)
        footer_layout.addWidget(footer_link)

        form_layout.addWidget(footer)
        main_layout.addWidget(form_container, alignment=Qt.AlignCenter)

    def clear_fields(self):
        """מאפס את שדות ההתחברות"""
        self.email_input.clear()
        self.password_input.clear()

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        result = self.presenter.login(email, password)

        if result:
            QMessageBox.information(self, "Success", "Welcome to the Library!")
            self.set_user(result)
            self.clear_fields()
            self.navigate_to("home")
        else:
            QMessageBox.warning(self, "Error", "Invalid email or password")
