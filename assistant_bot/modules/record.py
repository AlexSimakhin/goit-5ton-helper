"""
Модуль для зберігання та обробки записів контактів. 
Включає класи для роботи з ім'ям, номерами телефонів, 
електронними адресами, датою народження та фізичними адресами.
"""

from modules.email import Email
from modules.phone import Phone
from modules.name import Name
from modules.birthday import Birthday
from modules.address import Address

class Record:
    """
    Клас Record представляє запис контакту, що включає ім’я, номери телефонів,
    електронні адреси, дату народження та фізичні адреси.
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.addresses = []
        self.birthday = None

    def __str__(self):
        contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        emails = ', '.join(e.value for e in self.emails)
        addresses = ', '.join(a.value for a in self.addresses)
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"
        if emails:
            contact_info += f", emails: {emails}"
        if addresses:
            contact_info += f", addresses: {addresses}"
        return contact_info

    def add_phone(self, number: str):
        """Додає номер телефону до запису."""
        self.phones.append(Phone(number))

    def change_name(self, new_name):
        """Змінює номер телефону."""
        self.name = Name(new_name)

    def remove_phone(self, number: str):
        """Видаляє номер телефону з запису."""
        self.phones = list(filter(lambda phone: phone.value != number, self.phones))

    def edit_phone(self, old_number, new_number):
        """Редагує номер телефону в записі."""
        self.phones = list(
            map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones)
        )

    def find_phone(self, number):
        """Шукає номер телефону в записі."""
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def add_birthday(self, date):
        """Додає дату народження до запису."""
        self.birthday = Birthday(date)

    def add_email(self, email: Email):
        """Додає електронну пошту до запису."""
        self.emails.append(email)

    def edit_email(self, old_email, new_email):
        """Змінює електронну пошту."""
        for email in self.emails:
            if email.value == old_email:
                email.value = new_email
                return
        raise ValueError(f"Email '{old_email}' not found in contact.")

    def add_address(self, address: Address):
        """Додає адресу до запису."""
        self.addresses.append(address)
