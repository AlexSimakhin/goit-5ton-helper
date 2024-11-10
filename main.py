"""
Цей файл містить функції для роботи з адресною книгою та нотатками, включаючи додавання,
зміну, видалення контактів і нотаток, а також управління додатковими даними, такими як
телефонні номери, електронні адреси, дні народження та адреси. Функції обробляють
користувацький ввід, взаємодіють із класами:
`AddressBook`, `Notes`, `Record`, `Email`, `Address` та ін.,
забезпечуючи управління даними. 
"""

from email import Email
from address_book import AddressBook
from record import Record
from notes import Notes
from address import Address
from constants import NOT_FOUND_MESSAGE, COMMANDS
from data_storage import save_data, load_data, save_notes, load_notes


def parse_input(user_input):
    """Парсить введений користувачем рядок на команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    """Обробляє помилки для функцій з декоратором."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return str(error)
    return inner


@input_error
def add_contact(args, book: AddressBook):
    """Додає або оновлює контакт в адресній книзі."""
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    """Змінює номер телефону у записі контакту за старим номером."""
    if len(args) != 3:
        return "Invalid number of arguments. Usage: change [name] [old_number] [new_number]"
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        return NOT_FOUND_MESSAGE
    record.edit_phone(old_number, new_number)
    return "Phone changed"


@input_error
def delete_contact(args, book: AddressBook):
    """Видаляє контакт з адресної книги."""
    if len(args) != 1:
        return "Invalid number of arguments. Usage: delete [name]"
    name = args[0]
    record = book.find(name)
    if record is None:
        return NOT_FOUND_MESSAGE
    book.delete(name)
    return "Contact deleted."


@input_error
def show_phone(args, book: AddressBook):
    """Показує номер телефону контакту за його ім'ям."""
    if len(args) != 1:
        return "Invalid number of arguments. Usage: phone [name]"
    name = args[0]
    record = book.find(name)
    if record is None:
        return NOT_FOUND_MESSAGE
    return record


@input_error
def add_birthday(args, book: AddressBook):
    """Додає день народження до контакту."""
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add-birthday [name] [date]"
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    return NOT_FOUND_MESSAGE


@input_error
def get_birthdays_in_days(args, book: AddressBook):
    """Показує список днів народження в межах заданої кількості днів."""
    if len(args) != 1:
        return "Invalid number of arguments. Usage: birthdays [days]"
    days = int(args[0])
    return book.get_upcoming_birthdays(days)


@input_error
def add_email(args, book: AddressBook):
    """Додає email до контакту."""
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add-email [name] [email]"
    name, email = args
    record = book.find(name)
    email = Email(email)
    if record:
        record.add_email(email)
        return "Email added."
    return NOT_FOUND_MESSAGE


@input_error
def show_email(args, book: AddressBook):
    """Показує email контакту за його ім'ям."""
    if len(args) != 1:
        return "Invalid number of arguments. Usage: show-email [name]"
    name = args[0]
    record = book.find(name)
    if record:
        if record.emails:
            return record.emails
        return "Email not added to this contact."
    return NOT_FOUND_MESSAGE


@input_error
def add_address(args, book: AddressBook):
    """Додає адресу до контакту."""
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add-address [name] [address]"
    name, address = args
    record = book.find(name)
    address = Address(address)
    if record:
        record.add_address(address)
        return "Address added."
    return NOT_FOUND_MESSAGE


@input_error
def show_birthday(args, book: AddressBook):
    """Показує день народження контакту."""
    if len(args) != 1:
        return "Invalid number of arguments. Usage: show-birthday [name]"
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        return "Birthday not added to this contact."
    return NOT_FOUND_MESSAGE


@input_error
def add_note(notes: Notes):
    """Додає нову нотатку до списку нотаток."""
    title = input("Enter a title: ")
    if notes.find_note_by_title(title):
        return f"Note with title '{title}' already exists."
    text = input("Enter a text: ")
    tags = input("Enter tags (comma separated): ")
    try:
        notes.add_note(title, text, tags)
        return f"Note with title: '{title}' successfully added."
    except ValueError as e:
        return str(e)


@input_error
def show_all_notes(notes: Notes):
    """Показує всі нотатки."""
    return notes.show_all_notes()


@input_error
def change_note(notes: Notes):
    """Змінює зміст та теги існуючої нотатки."""
    title = input("Enter a title: ")
    new_content = input("Enter new content: ")
    new_tags = input("Enter new tags: ")
    note = notes.find_note_by_title(title)
    if note:
        if new_content:
            note.content = new_content
        if new_tags:
            note.tags = [tag.strip() for tag in new_tags.split(",")]
        return f"Note with title '{title}' successfully edited."
    else:
        return f"Note with title '{title}' not found."


@input_error
def delete_note(notes: Notes):
    """Видаляє нотатку за її заголовком."""
    title = input("Enter a title: ")
    note = notes.find_note_by_title(title)
    if note:
        notes.notes.remove(note)
        if notes.find_note_by_title(title):
            return f"Note with title: '{title}' not found."
        else:
            return f"Note with title: '{title}' successfully deleted."
    else:
        return f"Note with title: '{title}' not found."


@input_error
def find_note_by_title(notes: Notes):
    """Шукає нотатку за її заголовком."""
    title = input("Enter the title to search for: ")
    note = notes.find_note_by_title(title)
    if note:
        return note
    else:
        return f"Note with title '{title}' not found."


@input_error
def find_note_by_tag(notes: Notes):
    """Шукає нотатки за тегом."""
    tag = input("Enter the tag to search for: ")
    notes_with_tag = notes.find_note_by_tag(tag)
    if notes_with_tag:
        return "\n".join(str(note) for note in notes_with_tag)
    else:
        return f"No notes found with tag '{tag}'."


@input_error
def show_address(args, book: AddressBook):
    """Показує адресу контакту."""
    if len(args) != 1:
        return "Invalid number of arguments. Usage: show-address [name]"
    name = args[0]
    record = book.find(name)
    if record:
        if record.addresses:
            return record.addresses
        return "Address not added to this contact."
    return NOT_FOUND_MESSAGE


@input_error
def search_contact(args, book: AddressBook):
    """Шукає контакт за іменем."""
    if len(args) != 1:
        return "Invalid number of arguments. Usage: search [name]"
    name = args[0]
    record = book.find(name)
    if record:
        return str(record)
    return "No contacts found with that name"


def main():
    """
    Головна функція програми, яка ініціалізує адресну книгу та нотатки,
    потім запускає цикл, що обробляє ввід користувача.
    """

    book = load_data()
    notes = load_notes()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case cmd if cmd in COMMANDS["close"]:
                save_data(book)
                save_notes(notes)
                print("Good bye!")
                break
            case cmd if cmd in COMMANDS["hello"]:
                print("How can I help you?")
            case cmd if cmd in COMMANDS["add"]:
                print(add_contact(args, book))
            case cmd if cmd in COMMANDS["change"]:
                print(change_contact(args, book))
            case cmd if cmd in COMMANDS["delete"]:
                print(delete_contact(args, book))
            case cmd if cmd in COMMANDS["phone"]:
                print(show_phone(args, book))
            case cmd if cmd in COMMANDS["all"]:
                print(book)
            case cmd if cmd in COMMANDS["add-birthday"]:
                print(add_birthday(args, book))
            case cmd if cmd in COMMANDS["show-birthday"]:
                print(show_birthday(args, book))
            case cmd if cmd in COMMANDS["birthdays"]:
                print(book.get_upcoming_birthdays())
            case cmd if cmd in COMMANDS["add-note"]:
                print(add_note(notes))
            case cmd if cmd in COMMANDS["show-notes"]:
                print(show_all_notes(notes))
            case cmd if cmd in COMMANDS["change-note"]:
                print(change_note(notes))
            case cmd if cmd in COMMANDS["delete-note"]:
                print(delete_note(notes))
            case cmd if cmd in COMMANDS["find-note-by-title"]:
                print(find_note_by_title(notes))
            case cmd if cmd in COMMANDS["find-note-by-tag"]:
                print(find_note_by_tag(notes))
            case cmd if cmd in COMMANDS["birthdays-in-days"]:
                print(get_birthdays_in_days(args, book))
            case cmd if cmd in COMMANDS["add-email"]:
                print(add_email(args, book))
            case cmd if cmd in COMMANDS["email"]:
                print(show_email(args, book))
            case cmd if cmd in COMMANDS["add-address"]:
                print(add_address(args, book))
            case cmd if cmd in COMMANDS["address"]:
                print(show_address(args, book))
            case cmd if cmd in COMMANDS["search"]:
                print(search_contact(args, book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
