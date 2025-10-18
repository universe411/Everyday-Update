class Book:
    """Represents a physical book in the library."""

    def __init__(self, book_id: str, name: str, author: str, book_type: str):
        """Initialize book information."""
        self.book_id = book_id
        self.name = name
        self.author = author
        self.book_type = book_type
        self.is_available = True  # True if not borrowed

    def __str__(self):
        """Return a readable string of book details."""
        return (
            f"Book[{self.book_id}] {self.name} by {self.author} "
            f"({self.book_type}) - {'Available' if self.is_available else 'Borrowed'}"
        )


class EBook(Book):
    """Represents a digital version of a book."""

    def __init__(self, book_id: str, name: str, author: str, book_type: str, file_size_mb: int):
        """Initialize e-book information with file size."""
        super().__init__(book_id, name, author, book_type)
        self.file_size_mb = file_size_mb

    def __str__(self):
        """Return a readable string of e-book details."""
        return (
            f"[E-Book] {self.name} by {self.author} "
            f"({self.file_size_mb}MB, {self.book_type})"
        )
