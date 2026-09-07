"""
Student Grade Calculator
--------------------------
Assignment: Take marks as input, calculate average & assign grades.
"""


def calculate_average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks)


def assign_grade(average):
    """Return a letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def get_marks_from_user():
    """Prompt the user to enter marks for a number of subjects."""
    try:
        num_subjects = int(input("Enter the number of subjects: "))
    except ValueError:
        print("Invalid input.")
        return None

    if num_subjects <= 0:
        print("Number of subjects must be greater than zero.")
        return None

    marks = []
    for i in range(1, num_subjects + 1):
        try:
            mark = float(input(f"Enter marks for subject {i} (0-100): "))
        except ValueError:
            print("Invalid mark entered.")
            return None
        marks.append(mark)

    return marks


def main():
    print("=== Student Grade Calculator ===")

    marks = get_marks_from_user()
    if marks is None:
        return

    average = calculate_average(marks)
    grade = assign_grade(average)

    print(f"\nMarks entered: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
