import re
from field import Field  # Імпорт класу Field

class Email(Field):
    """
    Клас Email представляє поле для зберігання електронної пошти, успадковує клас Field.
    """

    def __init__(self, value: str) -> None:
        """
        Ініціалізує поле Email з електронною адресою, перевіряючи правильність формату.
        
        Параметри:
        - value (str): Електронна адреса у форматі рядка.
        
        Винятки:
        - ValueError: Якщо електронна адреса не відповідає вимогам.
        """
        self.__value = None
        self.value = value  # Викликає setter для валідації
        super().__init__(self.__value)  # Виклик конструктора батьківського класу Field

    @staticmethod
    def find_all_emails(text: str):
        """
        Знаходить усі коректні електронні адреси в переданому тексті.
        
        Параметри:
        - text (str): Текст, в якому здійснюється пошук електронних адрес.
        
        Повертає:
        - list: Список знайдених електронних адрес.
        """
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        return re.findall(pattern, text)

    @property
    def value(self) -> str:
        """
        Повертає значення електронної адреси.
        """
        return self.__value

    @value.setter
    def value(self, new_value: str) -> None:
        """
        Сеттер для значення електронної адреси, виконує валідацію.
        
        Параметри:
        - new_value (str): Нова електронна адреса для встановлення.
        
        Винятки:
        - ValueError: Якщо електронна адреса не відповідає вимогам.
        """
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", new_value):
            self.__value = new_value
        else:
            raise ValueError("Wrong email format")


class Phone(Field):
    """
    Клас Phone представляє поле для зберігання номера телефону, успадковує клас Field.
    """

    def __init__(self, number: str) -> None:
        """
        Ініціалізує поле Phone з номером телефону, перевіряючи правильність номера.
        
        Параметри:
        - number (str): Номер телефону у форматі рядка.
        
        Винятки:
        - ValueError: Якщо номер телефону не відповідає вимогам.
        """
        self.__value = self.validate_number(number)  # Валідація номера телефону
        super().__init__(self.__value)  # Виклик конструктора батьківського класу Field

    def validate_number(self, number: str) -> str:
        """
        Перевіряє правильність формату номера телефону.
        
        Параметри:
        - number (str): Номер телефону для перевірки.
        
        Повертає:
        - str: Перевірений номер телефону, якщо він відповідає вимогам.
        
        Винятки:
        - ValueError: Якщо номер телефону не містить рівно 10 цифр або містить нецифрові символи.
        """
        if not re.match(r"^\+?[\d\s\-\(\)]{10,15}$", number):
            raise ValueError("The phone number must contain only numbers and be in the correct format")

        digits_only = re.sub(r"\D", "", number)
        if len(digits_only) != 10:
            raise ValueError("The phone number must contain exactly 10 digits")

        return number
      
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, new_value: str) -> None:
        """
        Сеттер для значення номера телефону, виконує валідацію.
        """
        self.__value = self.validate_number(new_value)

    @staticmethod
    def is_phone(test_str: str) -> bool:
        """
        Перевіряє, чи є рядок коректним номером телефону.
        
        Параметри:
        - test_str (str): Номер телефону для перевірки.
        
        Повертає:
        - bool: True, якщо номер телефону коректний, False в іншому випадку.
        """
        regex = r"^\+?[\d\s\-\(\)]{10,15}$"
        return re.match(regex, test_str) is not None
