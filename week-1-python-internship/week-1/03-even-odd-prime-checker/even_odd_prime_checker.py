"""
Even/Odd & Prime Number Checker
----------------------------------
Assignment: Check whether a number is Even/Odd and whether it is Prime.
"""


def is_even(number):
    """Return True if the number is even, False otherwise."""
    return number % 2 == 0


def is_prime(number):
    """Return True if the number is a prime number, False otherwise."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    print("=== Even/Odd & Prime Number Checker ===")

    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    even_odd = "Even" if is_even(number) else "Odd"
    prime_status = "Prime" if is_prime(number) else "Not Prime"

    print(f"{number} is {even_odd}.")
    print(f"{number} is {prime_status}.")


if __name__ == "__main__":
    main()
