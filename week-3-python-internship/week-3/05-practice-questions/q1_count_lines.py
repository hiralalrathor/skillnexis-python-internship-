"""
Practice Q1: Read a file and count total lines.
"""


def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())


def main():
    print("=== Line Counter ===")
    filename = input("Enter the path to a text file (e.g. sample.txt): ").strip()

    try:
        total = count_lines(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    print(f"Total lines in '{filename}': {total}")


if __name__ == "__main__":
    main()
