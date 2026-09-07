"""
JSON File Reader
-------------------
Assignment: Load JSON data & print formatted output.
"""

import json


def load_json(filename):
    """Load and return data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def print_formatted(data):
    """Print the student records in a readable, formatted way."""
    students = data.get("students", [])

    if not students:
        print("No student records found.")
        return

    print(f"{'Name':<15}{'Roll No.':<12}{'Marks':<10}")
    print("-" * 35)
    for student in students:
        name = student.get("name", "N/A")
        roll = student.get("roll_number", "N/A")
        marks = student.get("marks", "N/A")
        print(f"{name:<15}{roll:<12}{marks:<10}")


def main():
    print("=== JSON File Reader ===")
    filename = input("Enter the path to a JSON file (e.g. sample_data.json): ").strip()

    try:
        data = load_json(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except json.JSONDecodeError:
        print("Error: File is not valid JSON.")
        return

    print_formatted(data)


if __name__ == "__main__":
    main()
