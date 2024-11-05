from address_book import AddressBook
from record import Record
from constants import NOT_FOUND_MESSAGE, COMMANDS
from data_storage import save_data, load_data


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return str(error)
    return inner


@input_error
def add_contact(args, book: AddressBook):
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
    if len(args) != 3:
        return "Invalid number of arguments. Usage: change [name] [old_number] [new_number]"
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        return NOT_FOUND_MESSAGE
    record.edit_phone(old_number, new_number)
    return "Phone changed"


@input_error
def show_phone(args, book: AddressBook):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: phone [name]"
    name = args[0]
    record = book.find(name)
    if record is None:
        return NOT_FOUND_MESSAGE
    return record


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add-birthday [name] [date]"    
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    return NOT_FOUND_MESSAGE


@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: show-birthday [name]"   
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        return "Birthday not added to this contact."
    return NOT_FOUND_MESSAGE


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case cmd if cmd in COMMANDS["close"]:
                save_data(book)
                print("Good bye!")
                break
            case cmd if cmd in COMMANDS["hello"]:
                print("How can I help you?")
            case cmd if cmd in COMMANDS["add"]:
                print(add_contact(args, book))
            case cmd if cmd in COMMANDS["change"]:
                print(change_contact(args, book))
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
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()