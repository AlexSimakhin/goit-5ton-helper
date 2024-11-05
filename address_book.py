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

    def get_upcoming_birthdays(self):
        """
        Знаходить контакти з днями народження, які відбудуться протягом наступного тижня.
        Якщо день народження припадає на вихідний, переносить привітання на наступний понеділок.
        
        Повертає:
        - List[Dict[str, str]]: Список словників з ім’ям контакту та датою привітання.
        """
        today = datetime.today().date()
        upcoming_birthdays = []
        for name, record in self.data.items():
            birthday = record.birthday
            if birthday:
                # Отримуємо день народження в поточному році
                birthday_this_year = birthday.value.replace(year=today.year).date()
                # Якщо день народження вже минув цього року, перевіряємо наступний рік
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                # Перевіряємо, чи потрапляє день народження в інтервал найближчого тижня
                days_until_birthday = (birthday_this_year - today).days
                if 0 <= days_until_birthday <= 7:
                    congratulation_date = birthday_this_year
                    # Переносимо на наступний понеділок, якщо день народження випадає на вихідні
                    if congratulation_date.weekday() == 5:  # Субота
                        congratulation_date += timedelta(days=2)
                    elif congratulation_date.weekday() == 6:  # Неділя
                        congratulation_date += timedelta(days=1)

                    # Додаємо контакт до списку
                    upcoming_birthdays.append({
                        "name": name,
                        "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
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
