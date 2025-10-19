from book import Book
from member import Member, VIPMember
from record import Record
from datetime import datetime


class Library:
    """Represents a library that manages books, members, and borrowing records."""

    default_due_in_days = 5  # default loan period for normal members

    def __init__(self):
        """Initialize empty collections for books, members, and records."""
        self.books = {}
        self.members = {}
        self.records = {}
        self.next_book_id = 1       # Auto-increment ID counters
        self.next_member_id = 1

    # ID Generation
    def generate_member_id(self) -> str:
        """Auto-generate a new unique member ID."""
        member_id = str(self.next_member_id)
        self.next_member_id += 1
        return member_id

    def generate_book_id(self) -> str:
        """Auto-generate a new unique book ID."""
        book_id = str(self.next_book_id)
        self.next_book_id += 1
        return book_id

    # Book and Member Management

    def add_book(self, book: Book):
        """Add a new book to the library."""
        if book.book_id in self.books:
            print("Book ID already exists.")
            return
        self.books[book.book_id] = book
        print(f"Book '{book.name}' added successfully (ID: {book.book_id}).")

    def add_member(self, member: Member):
        """Register a new member."""
        if member.member_id in self.members:
            print("Member ID already exists.")
            return
        self.members[member.member_id] = member
        print(
            f"Member '{member.name}' registered successfully (ID: {member.member_id}).")

    def find_book(self, book_id: str) -> Book:
        """Find and return a book by its ID."""
        return self.books.get(book_id)

    def find_member(self, member_id: str) -> Member:
        """Find and return a member by their ID."""
        return self.members.get(member_id)

    # Record Helper

    def find_active_record(self, member_id: str, book_id: str):
        """Find an active (not returned) record for given member and book."""
        for record in self.records.values():
            if (
                record.member_id == member_id
                and record.book_id == book_id
                and not record.is_returned()
            ):
                return record
        return None

    # Borrowing and Returning

    def borrow_book(self, book_id: str, member_id: str, borrow_date: str = None):
        """
        Borrow a book if it’s available.
        Creates a new record for the transaction.
        """
        # Check existence
        if book_id not in self.books:
            print("Book not found.")
            return
        if member_id not in self.members:
            print("Member not found.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        # Check if book is already borrowed
        for record in self.records.values():
            if record.book_id == book_id and not record.is_returned():
                print("Book has already been borrowed.")
                return

        # Use today if date not given
        if not borrow_date:
            borrow_date = datetime.now().strftime("%Y-%m-%d")

        record_id = f"record{len(self.records) + 1}"

        # Determine due days
        due_in_days = member.can_borrow_days()

        new_record = Record(record_id, borrow_date,
                            member_id, book_id, due_in_days)
        self.records[record_id] = new_record
        book.is_available = False

        print(f"Book '{book.name}' borrowed by {member.name} successfully.")

        # Adjust points (+5)
        self.adjust_points(member_id, +5)
        print(f"{member.name} earned +5 points (Total: {member.points}).")

    def return_book(self, record_id: str, return_date: str = None):
        """
        Return a borrowed book and calculate total fees.
        Deduct payment from member balance and adjust points.
        """
        if record_id not in self.records:
            print("record not found.")
            return

        record = self.records[record_id]
        member = self.members[record.member_id]
        book = self.books[record.book_id]

        # Use today if no date given
        if not return_date:
            return_date = datetime.now().strftime("%Y-%m-%d")

        daily_fee = member.get_daily_fee()
        total_fee = record.calculate_total_fee(return_date, daily_fee)

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
        book.is_available = True

        # Adjust points (-2)
        self.adjust_points(member.member_id, -2)
        print(f"{member.name}'s points adjusted (-2). Total: {member.points}")

    # Points Management

    def adjust_points(self, member_id: str, delta: int):
        """Increase or decrease member points (cannot go below 0)."""
        member = self.find_member(member_id)
        if not member:
            return
        member.points = max(0, member.points + delta)
