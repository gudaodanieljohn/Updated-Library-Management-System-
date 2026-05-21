from exception import BookUnavailableError

class Book:
    def __init__(self, book_id, title, author, isbn, year):
        self._book_id = book_id
        self.title = title 
        self._author = author
        self._isbn = isbn
        self._year = year
        self._is_available = True

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not value.strip():
            raise ValueError("Title cannot be empty")
        self._title = value.strip()

    @property
    def is_available(self):
        return self._is_available

    def mark_as_borrowed(self):
        if not self._is_available:
            raise BookUnavailableError(f"Book '{self.title}' is already borrowed.")
        self._is_available = False

    def mark_as_returned(self):
        self._is_available = True
        