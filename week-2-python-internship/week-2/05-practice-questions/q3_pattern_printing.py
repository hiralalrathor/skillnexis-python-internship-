"""
Practice Q3: Use nested loops to print a pattern.
"""


def print_pyramid(rows):
    """Print a simple star pyramid pattern with the given number of rows."""
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)


def main():
    print("=== Pattern Printer (Pyramid) ===")

    try:
        rows = int(input("Enter number of rows: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if rows <= 0:
        print("Number of rows must be positive.")
        return

    print_pyramid(rows)


if __name__ == "__main__":
    main()
