"""Модуль для визначення полів нотаток: Title, Content, Tags з перевірками валідності."""

from modules.field import Field

class Title(Field):
    """Поле для зберігання заголовка нотатки з перевіркою на порожнечу та обмеження по довжині."""

    def __init__(self, value):
        super().__init__(value)
        if not value:
            raise ValueError("Note title cannot be empty.")
        if len(value) > 255:
            raise ValueError("Note title cannot exceed 255 characters.")

class Content(Field):
    """Поле для зберігання вмісту нотатки з обмеженням по довжині."""

    def __init__(self, value):
        super().__init__(value)
        if len(value) > 255:
            raise ValueError("Note content cannot exceed 255 characters.")

class Tags(Field):
    """Поле для зберігання тегів нотатки з перевіркою на порожнечу та обмеження по довжині."""

    def __init__(self, value):
        super().__init__(value)
        if not value:
            raise ValueError("Note tags cannot be empty.")
        if len(value) > 255:
            raise ValueError("Note tags cannot exceed 255 characters.")
