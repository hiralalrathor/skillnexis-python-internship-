"""
Bank Account Class
----------------------
Assignment: Create a class with methods: deposit, withdraw, display balance.
"""


class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")

    def display_balance(self):
        print(f"Account holder: {self.owner_name}")
        print(f"Current balance: ₹{self.balance:.2f}")


def show_menu():
    print("\n=== Bank Account ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")


def main():
    print("=== Bank Account Class Demo ===")
    name = input("Enter account holder name: ").strip()
    account = BankAccount(name)

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-4.")


if __name__ == "__main__":
    main()
