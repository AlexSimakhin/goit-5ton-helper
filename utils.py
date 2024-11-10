"""Модуль для перевірок"""

import re

def is_valid_email(email):
    """Перевіряє, чи правильно відформатована електронна пошта."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(email_pattern, email))
