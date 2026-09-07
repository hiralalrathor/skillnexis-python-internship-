"""
Practice Q1: Create a list and perform CRUD operations.
"""

items = []


def create_item():
    value = input("Enter item to add: ").strip()
    items.append(value)
    print(f"Added: {value}")


def read_items():
    if not items:
        print("List is empty.")
        return
    for i, item in enumerate(items):
        print(f"{i}: {item}")


def update_item():
    read_items()
    try:
        index = int(input("Enter index to update: "))
        new_value = input("Enter new value: ").strip()
        items[index] = new_value
        print("Updated.")
    except (ValueError, IndexError):
        print("Invalid index.")


def delete_item():
    read_items()
    try:
        index = int(input("Enter index to delete: "))
        removed = items.pop(index)
        print(f"Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid index.")


def show_menu():
    print("\n=== List CRUD ===")
    print("1. Create (Add)")
    print("2. Read (View all)")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            create_item()
        elif choice == "2":
            read_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
