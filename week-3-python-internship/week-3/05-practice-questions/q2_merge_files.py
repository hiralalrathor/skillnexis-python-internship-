"""
Practice Q2: Write a program to merge two text files.
"""


def merge_files(file1, file2, output_file):
    with open(file1, "r", encoding="utf-8") as f1:
        content1 = f1.read()

    with open(file2, "r", encoding="utf-8") as f2:
        content2 = f2.read()

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(content1)
        out.write("\n")
        out.write(content2)


def main():
    print("=== Merge Two Text Files ===")
    file1 = input("Enter path to first file (e.g. file1.txt): ").strip()
    file2 = input("Enter path to second file (e.g. file2.txt): ").strip()
    output_file = input("Enter output filename (e.g. merged.txt): ").strip()

    try:
        merge_files(file1, file2, output_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    print(f"Files merged successfully into '{output_file}'.")


if __name__ == "__main__":
    main()
