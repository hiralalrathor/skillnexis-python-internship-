"""
Practice Q5: Sort a list using sort() and lambda key.
"""


def main():
    print("=== Sort List with Lambda Key ===")

    students = [
        {"name": "Aarav", "marks": 88},
        {"name": "Isha", "marks": 92},
        {"name": "Kabir", "marks": 76},
    ]

    print("Original list:")
    for s in students:
        print(s)

    # Sort by marks in descending order using sort() and a lambda key
    students.sort(key=lambda student: student["marks"], reverse=True)

    print("\nSorted by marks (highest first):")
    for s in students:
        print(s)


if __name__ == "__main__":
    main()
