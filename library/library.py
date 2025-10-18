from book import Book
from member import Member, VIPMember
from record import Record


class Library:
    """
    Represents a library that manages books, members, and borrowing records.
    """

    default_due_in_days = 5  # default loan period for normal members

    def __init__(self):
        """
        Initialize empty collections for books, members, and records.
        """
        self.books = {}
        self.members = {}
        self.records = {}

    # Book and Member Management
    def add_book(self, book: Book):
        """Add a new book to the library."""
        self.books[book.book_id] = book

    def add_member(self, member: Member):
        """Register a new member."""
        self.members[member.member_id] = member

    def find_book(self, book_id: str) -> Book:
        """Find and return a book by its ID."""
        return self.books.get(book_id)

    def find_member(self, member_id: str) -> Member:
        """Find and return a member by their ID."""
        return self.members.get(member_id)

    # -----------------------------
    # Borrowing and Returning
    # -----------------------------
    def borrow_book(self, book_id: str, member_id: str, borrow_date: str):
        """
        Borrow a book if its available.
        Creates a new record for the transaction.
        """
        # Check if book is already borrowed
        for record in self.records.values():
            if record.book_id == book_id and not record.is_returned():
                print("Book has already been borrowed.")
                return

        record_id = f"record{len(self.records) + 1}"

        # Determine loan period based on member type or points
        due_in_days = (
            30 if self.is_good(member_id) else self.default_due_in_days
        )

        new_record = Record(
            record_id, borrow_date, member_id, book_id, due_in_days
        )
        self.records[record_id] = new_record
        print(f"{book_id} borrowed by {member_id} successfully.")

    def is_good(self, member_id: str) -> bool:
        """Check if a member has enough points to get longer borrowing time."""
        member = self.find_member(member_id)
        return member and member.points >= 60

    def return_book(self, record_id: str, return_date: str):
        """
        Return a borrowed book and calculate total fees.
        Deduct payment from member balance.
        """
        if record_id not in self.records:
            print("Record not found.")
            return

        record = self.records[record_id]
        member = self.members[record.member_id]

        daily_fee = member.get_daily_fee()
        total_fee = record.calculate_total_fee(return_date, daily_fee)

        # Deduct from member balance
        if member.balance >= total_fee:
            member.balance -= total_fee
            print(
                f"{member.name} paid ${total_fee:.2f}. "
                f"Remaining balance: ${member.balance:.2f}"
            )
        else:
            print(
                f"{member.name} has insufficient balance. "
                f"Need ${total_fee:.2f}."
            )

        record.return_date = return_date
