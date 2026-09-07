"""
Contact Book using Dictionary
--------------------------------
Assignment: Add, search, update, delete contacts using a dictionary.
"""

contacts = {}


def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists. Use update instead.")
        return
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"Contact '{name}' added.")


def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"No contact found with name '{name}'.")


def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        contacts[name] = new_phone
        print(f"Contact '{name}' updated.")
    else:
        print(f"No contact found with name '{name}'.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found with name '{name}'.")


def view_all_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return
    print("\n--- All Contacts ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def show_menu():
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_all_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-6.")


if __name__ == "__main__":
    main()
