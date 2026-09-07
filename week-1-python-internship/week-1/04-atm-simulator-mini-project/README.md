# Mini Project (W1): Simple ATM Simulator

**Skill Gain:** Loops, conditionals, modular programming.

A command-line ATM simulator featuring:
- PIN-based login (3 attempts allowed)
- Check balance
- Deposit money
- Withdraw money (with insufficient-balance check)

Each operation is implemented as its own function, demonstrating
modular programming.

## Concepts Used
- Functions (modular programming)
- Loops (menu keeps running until exit)
- Conditional statements
- Global state management (account balance)
- Input validation

## How to Run
```bash
python atm_simulator.py
```
Default PIN for testing: `1234`

## Example
```
=== Welcome to the Simple ATM Simulator ===
Enter your 4-digit PIN: 1234
Login successful!

=== ATM Menu ===
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Choose an option (1-4): 1
Your current balance is: ₹5000.00
```

## Notes
This is a simplified simulation for learning purposes — the PIN and
balance are stored in memory only (no real database or persistence).
