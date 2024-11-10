"""Модуль для представлення адрес як поля запису."""

from field import Field

class Address(Field):
    """Клас для представлення адреси як окремого поля запису."""
    def __repr__(self):
        return str(self.value)
