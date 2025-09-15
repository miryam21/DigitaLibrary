from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


class LoginScreen(QWidget):
    def __init__(self, navigate_to):
        super().__init__()
        self.navigate_to = navigate_to
        self.setObjectName("LoginScreen")

        # לייאאוט ראשי
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setAlignment(Qt.AlignCenter)

        # קונטיינר של הטופס
        form_container = QFrame()
        form_container.setObjectName("FormContainer")
        form_layout = QVBoxLayout(form_container)
        form_layout.setSpacing(15)
        form_layout.setAlignment(Qt.AlignCenter)

        # כותרת
        title = QLabel("Start your reading..")
        title.setObjectName("LoginTitle")
        title.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title)

        # אימייל
        email_label = QLabel("Email Address")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setObjectName("LoginInput")
        self.email_input.addAction(QIcon("GUI/icons/email.png"), QLineEdit.LeadingPosition)

        # סיסמה
        password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setObjectName("LoginInput")
        self.password_input.addAction(QIcon("GUI/icons/password.png"), QLineEdit.LeadingPosition)

        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)

        # כפתור התחברות
        btn_login = QPushButton(" Sign In")
        btn_login.setObjectName("LoginButton")
        btn_login.setIcon(QIcon("GUI/icons/login.png"))
        btn_login.clicked.connect(lambda: print("Login clicked"))
        form_layout.addWidget(btn_login)

        # לינק לרישום
        footer = QFrame()
        footer_layout = QHBoxLayout(footer)
        footer_layout.setAlignment(Qt.AlignCenter)

        footer_text = QLabel("New here?")
        footer_link = QPushButton(" Create your Library Card")
        footer_link.setObjectName("LoginSwitchButton")
        footer_link.setIcon(QIcon("GUI/icons/register.png"))
        footer_link.clicked.connect(lambda: self.navigate_to("register"))

        footer_layout.addWidget(footer_text)
        footer_layout.addWidget(footer_link)

        form_layout.addWidget(footer)

        # מוסיפים את הטופס ללייאאוט הראשי
        main_layout.addWidget(form_container, alignment=Qt.AlignCenter)
