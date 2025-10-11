from services.auth_service import login_user, register_user

class AuthPresenter:
    def login(self, email: str, password: str):
        """מנסה להתחבר לשרת"""
        return login_user(email, password)

    def register(self, username: str, email: str, password: str):
        """מנסה לרשום משתמש חדש"""
        return register_user(username, email, password)
