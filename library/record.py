from datetime import datetime, timedelta


class Record:
    """Represents a single borrowing record."""

    def __init__(self, record_id: str, borrow_date: str,
                 member_id: str, book_id: str, due_in_days: int):
        """Initialize a record with borrow and due dates."""
        self.record_id = record_id
        self.borrow_date = borrow_date  # 'YYYY-MM-DD'
        self.member_id = member_id
        self.book_id = book_id
        self.return_date = None

        date_format = "%Y-%m-%d"
        borrow_date_obj = datetime.strptime(borrow_date, date_format)
        self.due_date = borrow_date_obj + timedelta(days=due_in_days)

    def is_returned(self) -> bool:
        """Return True if the book has been returned."""
        return self.return_date is not None

    def calculate_overdue_days(self, current_date: str) -> int:
        """Return number of overdue days (0 if not overdue)."""
        date_format = "%Y-%m-%d"
        current_date_obj = datetime.strptime(current_date, date_format)

        if self.return_date:
            actual_date = datetime.strptime(self.return_date, date_format)
        else:
            actual_date = current_date_obj

        overdue_days = (actual_date - self.due_date).days
        return max(overdue_days, 0)

    def calculate_overdue_fee(self, current_date: str, fee_per_day: int = 1) -> float:
        """Return overdue fee based on the given daily rate."""
        overdue_days = self.calculate_overdue_days(current_date)
        return overdue_days * fee_per_day if overdue_days > 0 else 0.0

    def calculate_total_fee(self, return_date: str, daily_fee: float, overdue_fee_per_day: int = 2) -> float:
        """Return total fee = normal days * daily fee + overdue days * overdue fee."""
        date_format = "%Y-%m-%d"
        borrow_date_obj = datetime.strptime(self.borrow_date, date_format)
        return_date_obj = datetime.strptime(return_date, date_format)
        total_days = (return_date_obj - borrow_date_obj).days

        overdue_days = self.calculate_overdue_days(return_date)
        overdue_fee = overdue_days * overdue_fee_per_day
        normal_fee = total_days * daily_fee

        return normal_fee + overdue_fee

    def __str__(self):
        """Return a readable summary of the record."""
        status = "Returned" if self.is_returned() else "Borrowed"
        return (
            f"Record[{self.record_id}] | Book: {self.book_id} | Member: {self.member_id} | "
            f"Borrowed: {self.borrow_date} | Due: {self.due_date.date()} | Status: {status}"
        )
