from field import Field
from utils import is_valid_email

class Email(Field):
    def __init__(self, email):
        """
        Ініціалізує поле Email зі значенням електронної пошти.
        
        Параметри:
        - email (str): Електронна пошта.
        """
        if not is_valid_email(email):
            raise ValueError("Invalid email format")
        super().__init__(email)
    def __repr__(self):
        return str(self.value)