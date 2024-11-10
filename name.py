"""Модуль для зберігання імені контакту з перевіркою значення."""

from field import Field

class Name(Field):
    """Поле для зберігання імені контакту, успадковує від Field."""

    def __init__(self, name):
        """Ініціалізує поле Name зі значенням імені. """
        self.value = name
