"""
Temperature Converter
-----------------------
Assignment: Convert Celsius <-> Fahrenheit using functions.
"""


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option (1 or 2): ").strip()

    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == "1":
        result = celsius_to_fahrenheit(value)
        print(f"{value}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(value)
        print(f"{value}°F = {result:.2f}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
