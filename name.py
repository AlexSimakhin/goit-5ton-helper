from field import Field

class Name(Field):
    """
    Клас Name представляє поле для зберігання імені контакту, успадковує клас Field.
    """

    def __init__(self, name):
        """
        Ініціалізує поле Name зі значенням імені.
        
        Параметри:
        - name (str): Ім’я контакту у форматі рядка.
        """
        self.value = name
