"""
Practice Q2: Write a dictionary program to count word frequency.
"""


def count_word_frequency(text):
    """Return a dictionary mapping each word to how many times it appears."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        cleaned = word.strip(".,!?;:\"'()")
        if cleaned:
            frequency[cleaned] = frequency.get(cleaned, 0) + 1
    return frequency


def main():
    print("=== Word Frequency Counter ===")
    text = input("Enter a sentence or paragraph: ")

    frequency = count_word_frequency(text)

    print("\nWord Frequencies:")
    for word, count in sorted(frequency.items(), key=lambda x: -x[1]):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
