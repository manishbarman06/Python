""" Polymorphism """

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return amount
        raise ValueError("Insufficient funds")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        # Savings account has no overdraft
        if amount <= self._balance:
            self._balance -= amount
            return amount
        raise ValueError("Insufficient funds")


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000

    def withdraw(self, amount):
        # Current account allows overdraft
        if amount <= self._balance + self.OVERDRAFT_LIMIT:
            self._balance -= amount
            return amount
        raise ValueError("Insufficient funds, overdraft limit exceeded")


# Polymorphism
accounts = [
    SavingsAccount(10000),
    CurrentAccount(10000)
]

for account in accounts:
    print(type(account).__name__)

    try:
        account.withdraw(12000)
        print(f"Balance: ₹{account.get_balance()}")
    except ValueError as e:
        print(e)