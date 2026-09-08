"""
Library Management System (OOP)
------------------------------------
Assignment: Add/remove books, issue/return books.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed.")
                return
        print(f"Book '{title}' not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    print(f"'{title}' is already issued.")
                else:
                    book.is_issued = True
                    print(f"'{title}' has been issued.")
                return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_issued:
                    print(f"'{title}' was not issued.")
                else:
                    book.is_issued = False
                    print(f"'{title}' has been returned.")
                return
        print(f"Book '{title}' not found.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print(f"\n{'Title':<25}{'Author':<20}{'Status':<10}")
        print("-" * 55)
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.title:<25}{book.author:<20}{status:<10}")


def show_menu():
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. Exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter book title to remove: ").strip()
            library.remove_book(title)
        elif choice == "3":
            title = input("Enter book title to issue: ").strip()
            library.issue_book(title)
        elif choice == "4":
            title = input("Enter book title to return: ").strip()
            library.return_book(title)
        elif choice == "5":
            library.view_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-6.")


if __name__ == "__main__":
    main()
