"""Модуль для представлення електронної пошти як поля."""

import re
from modules.field import Field

class Email(Field):
    """Поле для зберігання електронної пошти з перевіркою формату."""

    def __init__(self, email: str):
        """Ініціалізує поле Email зі значенням електронної пошти."""
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        super().__init__(email)

    def __repr__(self):
        """Повертає рядкове представлення електронної пошти."""
        return str(self.value)

    @staticmethod
    def is_valid_email(email):
        """Перевіряє, чи правильно відформатована електронна пошта."""
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))
