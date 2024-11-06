from collections import UserDict
from datetime import datetime, timedelta
from constants import DATE_FORMAT

class AddressBook(UserDict):
    """
    Клас AddressBook представляє телефонну книгу, яка успадковується від
    UserDict та містить записи контактів.
    """

    def add_record(self, record):
        """
        Додає запис (Record) до телефонної книги за ім’ям.
        
        Параметри:
        - record (Record): Об’єкт запису, що містить дані контакту.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Знаходить запис за ім’ям контакту.
        
        Параметри:
        - name (str): Ім’я контакту для пошуку.
        
        Повертає:
        - Record: Об’єкт запису, якщо контакт знайдено, або None, якщо не знайдено.
        """
        record = self.data.get(name, None)
        return record

    def delete(self, name):
        """
        Видаляє запис контакту за ім’ям.
        
        Параметри:
        - name (str): Ім’я контакту для видалення.
        
        Винятки:
        - KeyError: Якщо контакт з даним ім’ям не знайдено.
        """
        del self.data[name]

    def get_upcoming_birthdays(self, days: int = 7):
        """
        Знаходить контакти з днями народження, які відбудуться протягом наступного тижня.
        Якщо день народження припадає на вихідний, переносить привітання на наступний понеділок.
        
        Повертає:
        - List[Dict[str, str]]: Список словників з ім’ям контакту та датою привітання.
        """
        today = datetime.today().date()
        upcoming_birthdays = []
        records = self.data.values()

        for record in records:
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
                        "birthday_date": birthday_this_year.strftime('%d.%m.%Y')
                    })

        return upcoming_birthdays

    def __str__(self):
        """
        Повертає рядкове представлення всіх записів у телефонній книзі.
        
        Повертає:
        - str: Рядок зі списком усіх контактів.
        """
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines)
