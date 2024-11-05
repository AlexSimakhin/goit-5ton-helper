from field import Field

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

    def validate_number(self, number):
        """
        Перевіряє правильність формату номера телефону.
        
        Параметри:
        - number (str): Номер телефону для перевірки.
        
        Повертає:
        - str: Перевірений номер телефону, якщо він відповідає вимогам.
        
        Винятки:
        - ValueError: Якщо номер телефону не містить рівно 10 цифр або містить нецифрові символи.
        """
        if len(number) != 10:
            raise ValueError("The phone number must contain 10 digits")

        if not number.isdigit():
            raise ValueError("The phone number must contain only numbers")

        return number
