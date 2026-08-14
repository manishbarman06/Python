from abc import ABC, abstractmethod 

""" Abstract Class """
class BankAccount(ABC):
    def __init__(self, balance):
        self._balance = balance 

    @abstractmethod
    def withdraw(self, amount):
        pass

    """ Deposit Method """
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self._balance += amount 

    """ Get Balance Method """
    def get_balance(self):
        return self._balance 

""" Child Class """
class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount 
            return amount 

        raise ValueError("Insufficient Fund!")

""" Child Class """
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000
    def withdraw(self, amount):
        if amount <= self._balance + self.OVERDRAFT_LIMIT:
            self._balance -= amount 
            return amount 

        raise ValueError("Insufficient Fund!")

if __name__=="__main__":
    savings = SavingAccount(10000)
    current = CurrentAccount(10000)

    print("Savings Account")
    savings.withdraw(3000)
    print("Balance:", savings.get_balance())

    print("\nCurrent Account")
    current.withdraw(12000)
    print("Balance:", current.get_balance())




