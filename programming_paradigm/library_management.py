class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """A class representing the library, which manages books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book}")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book}")
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        """Print all available books."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        for book in available:
            print(book)
