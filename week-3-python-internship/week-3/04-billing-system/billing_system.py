"""
Mini Project (W3): Billing System (OOP-based)
--------------------------------------------------
Features:
- Product class -> attributes: name, price, quantity
- Bill class -> total calculation + tax
- Display final bill in tabular format

Skill Gain: Real-world class design, object interaction.
"""

TAX_RATE = 0.05  # 5% tax


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        subtotal = sum(p.subtotal() for p in self.products)
        tax = subtotal * TAX_RATE
        total = subtotal + tax
        return subtotal, tax, total

    def display_bill(self):
        if not self.products:
            print("No products added to the bill.")
            return

        print("\n" + "=" * 50)
        print(f"{'BILL':^50}")
        print("=" * 50)
        print(f"{'Product':<18}{'Price':<10}{'Qty':<8}{'Subtotal':<12}")
        print("-" * 50)

        for p in self.products:
            print(f"{p.name:<18}{p.price:<10.2f}{p.quantity:<8}{p.subtotal():<12.2f}")

        subtotal, tax, total = self.calculate_total()
        print("-" * 50)
        print(f"{'Subtotal:':<36}₹{subtotal:.2f}")
        print(f"{'Tax (5%):':<36}₹{tax:.2f}")
        print(f"{'Total:':<36}₹{total:.2f}")
        print("=" * 50)


def show_menu():
    print("\n=== Billing System ===")
    print("1. Add Product")
    print("2. Display Bill")
    print("3. Exit")


def main():
    print("=== Welcome to the Billing System ===")
    bill = Bill()

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter price per unit: "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid price or quantity.")
                continue
            product = Product(name, price, quantity)
            bill.add_product(product)
            print(f"'{name}' added to bill.")

        elif choice == "2":
            bill.display_bill()

        elif choice == "3":
            print("Thank you! Goodbye.")
            break

        else:
            print("Invalid option, please choose 1-3.")


if __name__ == "__main__":
    main()
