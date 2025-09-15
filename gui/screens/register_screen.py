from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


class RegisterScreen(QWidget):
    def __init__(self, navigate_to):
        super().__init__()
        self.navigate_to = navigate_to
        self.setObjectName("RegisterScreen")

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
        title = QLabel("Start Your Reading Journey")
        title.setObjectName("RegisterTitle")
        title.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title)

        # שם משתמש
        username_label = QLabel("Username")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Pick a nickname")
        self.username_input.setObjectName("RegisterInput")
        self.username_input.addAction(QIcon("GUI/icons/user.png"), QLineEdit.LeadingPosition)

        # אימייל
        email_label = QLabel("Email Address")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setObjectName("RegisterInput")
        self.email_input.addAction(QIcon("GUI/icons/email.png"), QLineEdit.LeadingPosition)

        # סיסמה
        password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Create a password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setObjectName("RegisterInput")
        self.password_input.addAction(QIcon("GUI/icons/password.png"), QLineEdit.LeadingPosition)

        # אישור סיסמה
        confirm_label = QLabel("Confirm Password")
        self.confirm_input = QLineEdit()
        self.confirm_input.setPlaceholderText("Repeat your password")
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setObjectName("RegisterInput")
        self.confirm_input.addAction(QIcon("GUI/icons/password.png"), QLineEdit.LeadingPosition)

        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(confirm_label)
        form_layout.addWidget(self.confirm_input)

        # כפתור הרשמה
        btn_register = QPushButton(" Join the Library")
        btn_register.setObjectName("RegisterButton")
        btn_register.setIcon(QIcon("GUI/icons/register.png"))
        btn_register.clicked.connect(lambda: print("Register clicked"))
        form_layout.addWidget(btn_register)

        # לינק חזרה ל־Login
        footer = QFrame()
        footer_layout = QHBoxLayout(footer)
        footer_layout.setAlignment(Qt.AlignCenter)

        footer_text = QLabel("Already a member?")
        footer_link = QPushButton(" Sign In")
        footer_link.setObjectName("RegisterSwitchButton")
        footer_link.setIcon(QIcon("GUI/icons/login.png"))
        footer_link.clicked.connect(lambda: self.navigate_to("login"))

        footer_layout.addWidget(footer_text)
        footer_layout.addWidget(footer_link)

        form_layout.addWidget(footer)

        # מוסיפים את הטופס ללייאאוט הראשי
        main_layout.addWidget(form_container, alignment=Qt.AlignCenter)
