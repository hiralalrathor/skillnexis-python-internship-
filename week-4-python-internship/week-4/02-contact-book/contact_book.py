"""
Mini Project Task: Contact Book app using dictionary.
"""

contacts = {}


def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added.")


def view_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return
    print("\n--- Contacts ---")
    for name, details in contacts.items():
        print(f"{name} | Phone: {details['phone']} | Email: {details['email']}")


def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"{name} | Phone: {details['phone']} | Email: {details['email']}")
    else:
        print(f"No contact found with name '{name}'.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found with name '{name}'.")


def show_menu():
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()
