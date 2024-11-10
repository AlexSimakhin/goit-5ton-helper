"""Модуль для зберігання, пошуку та управління контактами з нагадуванням про дні народження."""

from collections import UserDict
from datetime import datetime, timedelta
from utils.constants import DATE_FORMAT

class AddressBook(UserDict):
    """Телефонна книга для зберігання контактів."""

    def add_record(self, record):
        """Додає запис до книги."""
        self.data[record.name.value] = record

    def find(self, name):
        """Повертає запис контакту за ім’ям або None."""
        return self.data.get(name)

    def delete(self, name):
        """Видаляє запис за ім’ям (KeyError, якщо не знайдено)."""
        del self.data[name]

    def get_upcoming_birthdays(self, days: int = 7):
        """Повертає контакти з днями народження протягом вказаних днів."""
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value.date() if isinstance(record.birthday.value, datetime) else record.birthday.value
                birthday_this_year = birthday_date.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                days_until_birthday = (birthday_this_year - today).days

                if 0 <= days_until_birthday <= days:
                    if birthday_this_year.weekday() == 5:
                        birthday_this_year += timedelta(days=2)
                    elif birthday_this_year.weekday() == 6:
                        birthday_this_year += timedelta(days=1)
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday_date": birthday_this_year.strftime(DATE_FORMAT)
                    })

        return upcoming_birthdays

    def __str__(self):
        """Повертає всі записи у книзі як рядок."""
        return "\n".join(str(record) for record in self.data.values())
