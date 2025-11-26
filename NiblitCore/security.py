# security.py

class Security:

    @staticmethod
    def authenticate(token: str):
        return token == "dev"  # placeholder

    @staticmethod
    def has_permission(user="dev"):
        return True  # placeholder
