"""Модуль для збереження та завантаження даних адресної книги та нотаток за допомогою pickle."""

import pickle
import os
from address_book import AddressBook
from notes import Notes
from constants import FILE_DATA_PKL, FILE_NOTE_DATA_PKL

def save_data(book: AddressBook, filename=FILE_DATA_PKL):
    """Зберігає дані адресної книги у файл за допомогою pickle."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as file:
        pickle.dump(book, file)

def load_data(filename=FILE_DATA_PKL):
    """Завантажує дані адресної книги з файлу, або створює нову книгу, якщо файл не знайдено."""
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()

def save_notes(notes: Notes, filename=FILE_NOTE_DATA_PKL):
    """Зберігає нотатки у файл за допомогою pickle."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as file:
        pickle.dump(notes, file)

def load_notes(filename=FILE_NOTE_DATA_PKL):
    """Завантажує нотатки з файлу, або створює нові, якщо файл не знайдено."""
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return Notes()
