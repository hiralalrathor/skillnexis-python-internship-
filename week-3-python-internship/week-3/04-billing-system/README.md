# Mini Project (W3): Billing System (OOP-based)

**Skill Gain:** Real-world class design, object interaction.

An object-oriented billing system with two classes:
- **Product** — holds name, price, and quantity, and calculates its own subtotal
- **Bill** — holds a list of products, calculates tax and total, and
  displays the final bill in a tabular format

## Features
- Add multiple products to a bill
- Automatic subtotal calculation per product
- 5% tax applied to the overall subtotal
- Final bill displayed in a clean tabular format

## Concepts Used
- Classes and objects (two interacting classes)
- Object composition (`Bill` contains a list of `Product` objects)
- Methods and calculations
- Formatted table output

## How to Run
```bash
python billing_system.py
```

## Example
```
=== Billing System ===
1. Add Product
2. Display Bill
3. Exit
Choose an option (1-3): 1
Enter product name: Notebook
Enter price per unit: 50
Enter quantity: 3
'Notebook' added to bill.

Choose an option (1-3): 2

==================================================
                       BILL                       
==================================================
Product           Price     Qty     Subtotal    
--------------------------------------------------
Notebook          50.00     3       150.00      
--------------------------------------------------
Subtotal:                           ₹150.00
Tax (5%):                           ₹7.50
Total:                               ₹157.50
==================================================
```
