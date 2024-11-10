"""Модуль для представлення дати народження як поля з перевіркою формату."""

from datetime import datetime
from field import Field
from constants import DATE_FORMAT

class Birthday(Field):
    """Поле для зберігання дати народження контакту."""

    def __init__(self, value):
        """Ініціалізує дату народження у форматі DD.MM.YYYY."""
        try:
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        """Повертає дату народження у форматі DD.MM.YYYY."""
        return self.value.strftime(DATE_FORMAT)
