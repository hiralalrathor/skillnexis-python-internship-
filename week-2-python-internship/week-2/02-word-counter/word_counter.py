"""
Word Counter from Text File
-------------------------------
Assignment: Count number of words, lines, and characters in a text file.
"""


def count_file_stats(filename):
    """Return (line_count, word_count, char_count) for the given file."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    return line_count, word_count, char_count


def main():
    print("=== Word Counter from Text File ===")
    filename = input("Enter the path to a text file (e.g. sample.txt): ").strip()

    try:
        lines, words, chars = count_file_stats(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    print(f"\nFile: {filename}")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")


if __name__ == "__main__":
    main()
