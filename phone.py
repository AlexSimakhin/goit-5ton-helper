from field import Field
import re

class Phone(Field):
    """
    Клас Phone представляє поле для зберігання номера телефону, успадковує клас Field.
    """

    def __init__(self, number):
        """
        Ініціалізує поле Phone з номером телефону, перевіряючи правильність номера.
        
        Параметри:
        - number (str): Номер телефону у форматі рядка.
        
        Винятки:
        - ValueError: Якщо номер телефону не відповідає вимогам.
        """
        self.value = self.validate_number(number)


    def validate_number(self, number: str) -> str:
        if not re.match(r"^\+380\d{9}$", number):
            raise ValueError("Номер телефону повинен починатися з '+380' та містити загалом 12 цифр")
        
        return number
