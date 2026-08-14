# Parent class
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")


# Child class 1
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print(f"Interest added: ₹{interest}")


# Child class 2
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Current account allows an overdraft of ₹5,000
        if amount <= self.balance + 5000:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Withdrawal limit exceeded.")


# Using SavingsAccount
savings = SavingsAccount("SA101", "Rahul", 10000)

savings.display_balance()
savings.deposit(5000)
savings.withdraw(2000)
savings.add_interest(5)
savings.display_balance()


print("\n------------------\n")


# Using CurrentAccount
current = CurrentAccount("CA101", "Amit", 5000)

current.display_balance()
current.withdraw(8000)
current.display_balance()