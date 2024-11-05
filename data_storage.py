import pickle
from address_book import AddressBook
from constants import FILE_DATA_PKL

def save_data(book, filename=FILE_DATA_PKL):
    """
    Надійно зберігає дані адресної книги у файл за допомогою модуля pickle.
    
    Параметри:
    - book (AddressBook): Об’єкт адресної книги, який потрібно зберегти.
    - filename (str): Ім’я файлу, в який зберігаються дані. За замовчуванням використовується значення FILE_DATA_PKL.
    """
    with open(filename, "wb") as file:
        pickle.dump(book, file)

def load_data(filename=FILE_DATA_PKL):
    """
    Завантажує дані адресної книги з файлу за допомогою модуля pickle.
    
    Параметри:
    - filename (str): Ім’я файлу, з якого завантажуються дані. За замовчуванням використовується значення FILE_DATA_PKL.
    
    Повертає:
    - AddressBook: Об’єкт адресної книги. Якщо файл не знайдено, повертає новий, порожній об’єкт AddressBook.
    """
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
