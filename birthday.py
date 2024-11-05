from datetime import datetime
from field import Field
from constants import DATE_FORMAT

class Birthday(Field):
    """
    Клас Birthday представляє поле для зберігання дати народження контакту.
    """

    def __init__(self, value):
        """
        Ініціалізує поле Birthday, перетворюючи рядок у об'єкт datetime 
        за вказаним форматом.
        
        Параметри:
        - value (str): Дата народження у форматі рядка.
        
        Винятки:
        - ValueError: Якщо формат дати не відповідає вимогам (DD.MM.YYYY).
        """
        try:
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        """
        Повертає рядкове представлення дати народження у форматі, 
        визначеному константою DATE_FORMAT.
        
        Повертає:
        - str: Дата народження у форматі рядка.
        """
        return f"{self.value.strftime(DATE_FORMAT)}"
