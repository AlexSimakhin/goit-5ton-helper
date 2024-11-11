"""Модуль для зберігання моб. номера контакта з перевіркою."""
import re
from modules.field import Field

class Phone(Field):
    """
    Клас Phone представляє поле для зберігання номера телефону, успадковує клас Field.
    """

    def __init__(self, number):
        """
        Ініціалізує поле Phone з номером телефону, перевіряючи правильність номера.
        """
        self.value = self.validate_number(number)


    def validate_number(self, number: str) -> str:
        """
        Перевіряка правильності номера.
        """
        if not re.match(r"^\+380\d{9}$", number):
            raise ValueError("Номер телефону повинен починатися з '+380' та містити загалом 12 цифр")

        return number
