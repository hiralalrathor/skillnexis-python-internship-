"""
Practice Q4: Find largest and smallest number in a list.
"""


def find_largest_smallest(numbers):
    """Return (largest, smallest) from a list of numbers."""
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest


def main():
    print("=== Largest & Smallest Number Finder ===")
    raw_input_str = input("Enter numbers separated by spaces: ")

    try:
        numbers = [float(x) for x in raw_input_str.split()]
    except ValueError:
        print("Please enter valid numbers only.")
        return

    if not numbers:
        print("No numbers entered.")
        return

    largest, smallest = find_largest_smallest(numbers)
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")


if __name__ == "__main__":
    main()
