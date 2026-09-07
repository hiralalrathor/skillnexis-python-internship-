"""
Mini Project (W2): Student Management System
-------------------------------------------------
Features:
- Store student data (name, marks, roll number) in a CSV file
- Add / Delete / Search functions
- Save changes permanently to file

Skill Gain: Data storage, file I/O, CRUD logic.
"""

import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["roll_number", "name", "marks"]


def init_file():
    """Create the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_all_students():
    """Return a list of all student records from the CSV file."""
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_all_students(students):
    """Overwrite the CSV file with the given list of student records."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    """Add a new student record and save it to the file."""
    roll_number = input("Enter roll number: ").strip()
    students = read_all_students()

    if any(s["roll_number"] == roll_number for s in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter name: ").strip()
    marks = input("Enter marks: ").strip()

    students.append({"roll_number": roll_number, "name": name, "marks": marks})
    write_all_students(students)
    print(f"Student '{name}' added and saved.")


def delete_student():
    """Delete a student record by roll number."""
    roll_number = input("Enter roll number to delete: ").strip()
    students = read_all_students()

    filtered = [s for s in students if s["roll_number"] != roll_number]

    if len(filtered) == len(students):
        print(f"No student found with roll number '{roll_number}'.")
        return

    write_all_students(filtered)
    print(f"Student with roll number '{roll_number}' deleted and saved.")


def search_student():
    """Search for a student record by roll number."""
    roll_number = input("Enter roll number to search: ").strip()
    students = read_all_students()

    for s in students:
        if s["roll_number"] == roll_number:
            print(f"Found: Roll No {s['roll_number']}, Name: {s['name']}, Marks: {s['marks']}")
            return

    print(f"No student found with roll number '{roll_number}'.")


def view_all_students():
    """Display all student records."""
    students = read_all_students()

    if not students:
        print("No student records found.")
        return

    print(f"\n{'Roll No.':<12}{'Name':<20}{'Marks':<10}")
    print("-" * 42)
    for s in students:
        print(f"{s['roll_number']:<12}{s['name']:<20}{s['marks']:<10}")


def show_menu():
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. View All Students")
    print("5. Exit")


def main():
    init_file()
    print("=== Welcome to the Student Management System ===")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()
