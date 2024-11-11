"""Модуль для зберігання налаштувань."""

DATE_FORMAT = "%d.%m.%Y"

FILE_DATA_PKL = "goit-5ton-helper/addressbook.pkl"
FILE_NOTE_DATA_PKL = "goit-5ton-helper/notes.pkl"

NOT_FOUND_MESSAGE = "Contact does not exist, you can add it"

COMMANDS = {
  "close": {"close", "exit", "leave", "вийти", "закрити", ""},
  "hello": {"hello", "привіт", "здрастуйте", "доброго дня"},
  "add": {"add", "додати", "створити"},
  "change-contact": {"change-contact", "змінити-контакт"},
  "delete": {"delete", "remove", "видалити", "стерти"},
  "phone": {"phone", "телефон"},
  "all": {"all", "усі", "все"},
  "add-birthday": {"add-birthday", "додати-день-народження"},
  "show-birthday": {"show-birthday", "показати-день-народження"},
  "birthdays": {"birthdays", "дні-народження"},
  "add-note": {"add-note", "додати-нотатку"},
  "show-notes": {"show-notes", "show-all-notes", "показати-нотатки", "показати-усі-нотатки"},
  "change-note": {"change-note", "змінити-нотатку"},
  "delete-note": {"delete-note", "remove-note", "видалити-нотатку"},
  "find-note-by-title": {"find-note-by-title", "знайти-нотатку-за-заголовком"},
  "find-note-by-tag": {"find-note-by-tag", "знайти-нотатку-за-тегом"},
  "birthdays-in-days": {"birthdays-in-days", "дні-народження-за-днів"},
  "add-address": {"add-address", "додати-адресу"},
  "address": {"address", "адреса"},
  "add-email": {"add-email", "додати-електронну-пошту"},
  "email": {"email", "пошта", "електронна-пошта"},
  "search": {"search", "find", "пошук", "знайти"},
}

