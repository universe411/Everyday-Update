from library import Library
from member import Member
from book import Book
from datetime import datetime
from enum import Enum


# enum defines book types
class BookType(Enum):
    NOVEL = "Novel"
    SCIFI = "Sci-Fi"
    HISTORY = "History"
    OTHER = "Other"


# This function asks user for a phone number
# phone number must be 10 digits or it is invalid
def input_phone():
    phone = input("Enter phone number (10 digits): ")
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number format.")
        return None
    return phone


# makes sure user enters a positive number
def input_positive_float(prompt: str):
    try:
        amount = float(input(prompt))
        if amount <= 0:
            print("Amount must be positive.")
            return None
        return amount
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def main():
    # Create a Library object to manage books, members, and records
    library = Library()

    # 1: Register a new member

    def register_member():
        # System automatically gives an ID
        member_id = library.generate_member_id()
        name = input("Enter member name: ")
        phone = input_phone()
        if not phone:
            return  # Stop if phone is invalid
        member = Member(member_id, name, phone)
        library.add_member(member)

    # 2. Recharge balance for a member
    def recharge_member():
        member_id = input("Enter member ID: ")
        member = library.find_member(member_id)
        if not member:
            print("Member not found.")
            return
        amount = input_positive_float("Enter recharge amount: ")
        if amount:
            member.recharge(amount)
            print(f"{member.name}'s new balance: ${member.balance:.2f}")

    # 3. Upgrade member to VIP
    def upgrade_member():
        member_id = input("Enter member ID: ")
        member = library.find_member(member_id)
        if not member:
            print("Member not found.")
            return
        new_member = member.upgrade_to_vip()
        library.members[member_id] = new_member  # replace the old member
        print(f"{member.name} upgraded to VIP successfully.")

    # 4: Add a new book
    def add_book():
        # System automatically gives book ID
        book_id = library.generate_book_id()
        name = input("Enter book name: ")
        author = input("Enter author: ")

        print("Select book type:")
        print("1. Novel  2. Sci-Fi  3. History  4. Other")
        type_choice = input("Choose (1-4): ")

        # Match the number to a type
        book_type = BookType.NOVEL
        if type_choice == "2":
            book_type = BookType.SCIFI
        elif type_choice == "3":
            book_type = BookType.HISTORY
        elif type_choice == "4":
            book_type = BookType.OTHER

        book = Book(book_id, name, author, book_type.value)
        library.add_book(book)

    # 5: Borrow a book
    def borrow_book():
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")

        # System uses today’s date automatically
        borrow_date = datetime.now().strftime("%Y-%m-%d")
        library.borrow_book(book_id, member_id, borrow_date)

    # 6: Return a book
    def return_book():
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")

        # Find the record that matches this member and book
        record = library.find_active_record(member_id, book_id)
        if not record:
            print("No active borrow record found.")
            return

        # System uses today’s date automatically
        return_date = datetime.now().strftime("%Y-%m-%d")
        library.return_book(record.record_id, return_date)

    # 7: View one member’s information
    def view_member():
        member_id = input("Enter member ID: ")
        member = library.find_member(member_id)
        if member:
            print(member)
        else:
            print("Member not found.")

    # 8: View all books
    def view_books():
        if not library.books:
            print("No books in the library yet.")
            return
        print("\n--- Book List ---")
        for book in library.books.values():
            print(book)

    # 9: View all borrow records
    def view_records():
        if not library.records:
            print("No records yet.")
            return
        print("\n--- Borrow Records ---")
        for record in library.records.values():
            print(record)

    # Create a dictionary to connect numbers to functions
    # This makes the menu cleaner (no long if-elif chain)
    actions = {
        "0": lambda: exit(print("Goodbye!")),
        "1": register_member,
        "2": recharge_member,
        "3": upgrade_member,
        "4": add_book,
        "5": borrow_book,
        "6": return_book,
        "7": view_member,
        "8": view_books,
        "9": view_records,
    }

    # Main program loop
    while True:
        print("\n=== Library System ===")
        print("0. Exit")
        print("1. Register Member")
        print("2. Recharge Balance")
        print("3. Upgrade to VIP")
        print("4. Add Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. View Member Info")
        print("8. View All Books")
        print("9. View All Records")

        # Get user choice
        choice = input("Choose an option (0-9): ")

        # Run the corresponding function
        # If input not in menu, print error
        action = actions.get(choice, lambda: print("Invalid option."))
        action()


if __name__ == "__main__":
    main()
