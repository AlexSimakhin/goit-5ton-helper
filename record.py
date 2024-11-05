from phone import Phone
from name import Name
from birthday import Birthday

class Record:
    """
    Клас Record представляє запис контакту, що включає ім’я, номери телефонів 
    та дату народження.
    """

    def __init__(self, name):
        """
        Ініціалізує запис з ім'ям, порожнім списком телефонів та полем для дати народження.
        
        Параметри:
        - name (str): Ім’я контакту.
        """
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        """
        Повертає рядкове представлення запису, включаючи ім'я, телефони та дату народження, якщо є.
        
        Повертає:
        - str: Рядок з інформацією про контакт.
        """
        contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        # Додає дату народження, якщо вона вказана.
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"
        return contact_info

    def add_phone(self, number: str):
        """
        Додає номер телефону до запису.
        
        Параметри:
        - number (str): Номер телефону для додавання.
        """
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        """
        Видаляє номер телефону із запису.
        
        Параметри:
        - number (str): Номер телефону, який потрібно видалити.
        """
        self.phones = list(filter(lambda phone: phone.value != number, self.phones))

    def edit_phone(self, old_number, new_number):
        """
        Редагує номер телефону у записі, замінюючи старий номер на новий.
        
        Параметри:
        - old_number (str): Номер телефону, який потрібно змінити.
        - new_number (str): Новий номер телефону для заміни.
        """
        self.phones = list(
            map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones)
        )

    def find_phone(self, number):
        """
        Знаходить номер телефону у записі.
        
        Параметри:
        - number (str): Номер телефону для пошуку.
        
        Повертає:
        - Phone: Об’єкт телефону, якщо знайдено, або None, якщо не знайдено.
        """
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def add_birthday(self, date):
        """
        Додає дату народження до запису.
        
        Параметри:
        - date (str): Дата народження у форматі, визначеному константою DATE_FORMAT.
        """
        self.birthday = Birthday(date)
