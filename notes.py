from fields_notes import Title, Content

class Note:
    def __init__(self, title, content=None, tags=None):
        if not title:
            raise ValueError("Title is required")
        self.title = Title(title)
        self.content = Content(content)
        self.tags = tags if tags else []

    def __str__(self) -> str:
        title_str = f"Title: {self.title.value}"
        content_str = f"Content: {self.content}" if self.content else ""
        return "\n".join(filter(None, [title_str, content_str]))


class Notes:
    def __init__(self):
        self.notes = []

    def add_note(self, title, text=None):
        if self.find_note_by_title(title):
            raise ValueError(f"Note with title: '{title}' already exists.")
        note = Note(title, text)
        self.notes.append(note)
        return f"Note with title: '{title}' successfully added."

    def find_note_by_title(self, title):
        if not title:
            raise ValueError("Title is required")
        for note in self.notes:
            if note.title.value == title:
                return note
        return None

    def show_all_notes(self):
        if not self.notes:
            return "No notes available."

        divider_str = "-" * 40
        notes_str = "\n\n".join(f"{divider_str}\n{note}\n{divider_str}" for note in self.notes)
        return notes_str
