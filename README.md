# GoIT 5Ton Helper Bot

GoIT 5Ton Helper Bot is a command-line personal assistant designed to streamline and automate common tasks. This bot can manage contacts, schedule reminders, and store notes, making it a helpful tool for daily task management.

## Features

The GoIT 5Ton Helper Bot provides the following functionalities:

1. **Contact Book Management**
   - Save contacts with names, addresses, phone numbers, emails, and birthdays.
   - Display a list of contacts with upcoming birthdays within a specified number of days.
   - Validate phone numbers and emails upon creation or editing, with notifications for incorrect entries.
   - Search, edit, and delete entries from the contact book.

2. **Notes Management**
   - Save and store text notes with various details.
   - Search through saved notes for specific information.
   - Edit and delete notes as needed.


## Commands
| Command                   | Arguments            | Description                                                       |
|---------------------------|----------------------|-------------------------------------------------------------------|
| `hello`                   | no arguments         | Greeting.                                                         |
| `close` or `exit`         | no arguments         | Stops the bot.                                                    |
| `add`                     | `name, details`      | Adds a contact with the specified name and details.               |
| `change`                  | `name, new details`  | Updates an existing contact's details.                            |
| `delete`                  | `name`               | Removes a contact by name.                                        |
| `phone`                   | `name`               | Shows the phone number for a specific contact.                    |
| `all`                     | no arguments         | Displays all contacts.                                            |
| `add-birthday`            | `name, birthday`     | Adds a birthday for a specific contact.                           |
| `show-birthday`           | `name`               | Displays the birthday of a contact.                               |
| `birthdays`               | no arguments         | Shows contacts with upcoming birthdays.                           |
| `birthdays-in-days`       | `days`               | Lists contacts with birthdays within the specified number of days.|
| `add-note`                | `title, content`     | Adds a note with a title and content.                             |
| `show-notes`              | no arguments         | Shows all saved notes.                                            |
| `change-note`             | `title, new content` | Updates the content of an existing note.                          |
| `delete-note`             | `title`              | Deletes a note by title.                                          |
| `find-note-by-title`      | `title`              | Searches for a note by its title.                                 |
| `find-note-by-tag`        | `tag`                | Searches for notes by a specific tag.                             |
| `add-email`               | `name, email`        | Adds an email for a specific contact.                             |
| `email`                   | `name`               | Shows the email for a specific contact.                           |
| `add-address`             | `name, address`      | Adds an address for a specific contact.                           |
| `address`                 | `name`               | Shows the address for a specific contact.                         |
| `search`                  | `query`              | Searches contacts by name or other criteria.                      |



## Installation

Ensure you have `setuptools` and `prompt_toolkit` installed:

```bash
pip install setuptools prompt_toolkit
```

The last command will install package and you will be able to use it anywhere

```bash
pip install -e .
```