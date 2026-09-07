"""
Mini Project (W1): Simple ATM Simulator
------------------------------------------
Features:
- User login (PIN-based)
- Options: check balance, deposit, withdraw
- Each operation implemented as its own function (modular programming)
"""

# Preset account details (in a real system this would come from a database)
CORRECT_PIN = "1234"
balance = 5000.0  # starting balance


def login():
    """Ask the user for a PIN and validate it. Returns True/False."""
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
    print("Too many incorrect attempts. Exiting.")
    return False


def check_balance():
    """Display the current account balance."""
    print(f"Your current balance is: ₹{balance:.2f}")


def deposit():
    """Deposit money into the account."""
    global balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Deposit amount must be positive.")
        return

    balance += amount
    print(f"₹{amount:.2f} deposited successfully.")
    check_balance()


def withdraw():
    """Withdraw money from the account, if sufficient balance exists."""
    global balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return

    if amount > balance:
        print("Insufficient balance.")
        return

    balance -= amount
    print(f"₹{amount:.2f} withdrawn successfully.")
    check_balance()


def show_menu():
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    print("=== Welcome to the Simple ATM Simulator ===")

    if not login():
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
