from library import Library
from member import Member
from book import Book


def input_numeric_id(prompt: str):
    """Force user to input a numeric ID."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return user_input
        else:
            print("❌ ID must be numeric. Please try again.")


def main():
    library = Library()

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

        choice = input("Choose an option (0-9): ")

        # 0. Exit
        if choice == "0":
            print("886! 👋")
            break

        # 1. Register Member
        elif choice == "1":
            member_id = input_numeric_id("Enter member ID (numbers only): ")

            # 检查重复
            if member_id in library.members:
                print("❌ Member ID already exists.")
                continue

            name = input("Enter name: ")
            phone = input("Enter phone number: ")

            member = Member(member_id, name, phone)
            library.add_member(member)
            print(f"✅ Member '{name}' registered successfully.")

        # 2. Recharge
        elif choice == "2":
            member_id = input_numeric_id("Enter member ID: ")
            member = library.find_member(member_id)
            if not member:
                print("❌ Member not found.")
                continue
            try:
                amount = float(input("Enter amount to recharge: "))
                if amount <= 0:
                    print("❌ Amount must be positive.")
                    continue
            except ValueError:
                print("❌ Invalid number.")
                continue

            member.recharge(amount)

        # 3. Upgrade to VIP
        elif choice == "3":
            member_id = input_numeric_id("Enter member ID: ")
            member = library.find_member(member_id)
            if not member:
                print("❌ Member not found.")
                continue
            new_member = member.upgrade_to_vip()
            library.members[member_id] = new_member  # 替换为 VIP

        # 44. add Book
        elif choice == "4":
            book_id = input_numeric_id("Enter book ID (numbers only): ")

            # 检查重复
            if book_id in library.books:
                print("❌ Book ID already exists.")
                continue

            name = input("Enter book name: ")
            author = input("Enter author: ")
            book_type = input("Enter type (e.g. Novel, Sci-Fi): ")

            book = Book(book_id, name, author, book_type)
            library.add_book(book)
            print(f"✅ Book '{name}' added successfully.")

        # 5. Borrow Book
        elif choice == "5":
            book_id = input_numeric_id("Enter book ID: ")
            member_id = input_numeric_id("Enter member ID: ")
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            library.borrow_book(book_id, member_id, borrow_date)

        # 6. Return Book
        elif choice == "6":
            member_id = input_numeric_id("Enter member ID: ")
            book_id = input_numeric_id("Enter book ID: ")
            return_date = input("Enter return date (YYYY-MM-DD): ")

            # 查找未归还记录
            found_record = None
            for record in library.records.values():
                if (
                    record.member_id == member_id
                    and record.book_id == book_id
                    and not record.is_returned()
                ):
                    found_record = record
                    break

            if not found_record:
                print("❌ No active borrow record found for this member and book.")
                continue

            library.return_book(found_record.record_id, return_date)

        # 7. View Member Info
        elif choice == "7":
            member_id = input_numeric_id("Enter member ID: ")
            member = library.find_member(member_id)
            if member:
                print(member)
            else:
                print("❌ Member not found.")

        # 8. View All Books
        elif choice == "8":
            if not library.books:
                print("📚 No books in the library yet.")
            else:
                print("\n--- Book List ---")
                for book in library.books.values():
                    print(book)

        # View All Records
        elif choice == "9":
            if not library.records:
                print(" No records yet.")
            else:
                print("\n--- Borrow Records ---")
                for record in library.records.values():
                    print(record)

        else:
            print("❌ Invalid option. Please enter 0-9.")


if __name__ == "__main__":
    main()
