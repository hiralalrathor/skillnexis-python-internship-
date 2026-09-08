"""
Calculator Class with Exception Handling
---------------------------------------------
Assignment: Calculator Class with Exception Handling.
"""


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def main():
    print("=== Calculator Class with Exception Handling ===")
    calc = Calculator()

    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = calc.add(num1, num2)
        elif operator == "-":
            result = calc.subtract(num1, num2)
        elif operator == "*":
            result = calc.multiply(num1, num2)
        elif operator == "/":
            result = calc.divide(num1, num2)
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
