"""Модуль для представлення електронної пошти як поля."""

from field import Field
from utils import is_valid_email

class Email(Field):
    """Поле для зберігання електронної пошти з перевіркою формату."""

    def __init__(self, email: str):
        """Ініціалізує поле Email зі значенням електронної пошти."""
        if not is_valid_email(email):
            raise ValueError("Invalid email format")
        super().__init__(email)

    def __repr__(self):
        """Повертає рядкове представлення електронної пошти."""
        return str(self.value)
