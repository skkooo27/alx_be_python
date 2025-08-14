class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrew: ${amount:.2f}"

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
