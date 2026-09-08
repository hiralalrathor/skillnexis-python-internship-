"""
Practice Q5: Create a JSON file and read data from it.
"""

import json


def create_json_file(filename):
    data = {
        "students": [
            {"name": "Aarav", "grade": "A"},
            {"name": "Isha", "grade": "A+"},
            {"name": "Kabir", "grade": "B"},
        ]
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"JSON file '{filename}' created.")


def read_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\n--- Data read from JSON file ---")
    for student in data.get("students", []):
        print(f"{student['name']}: {student['grade']}")


def main():
    print("=== Create & Read JSON File ===")
    filename = "students_output.json"

    create_json_file(filename)
    read_json_file(filename)


if __name__ == "__main__":
    main()
