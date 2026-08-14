class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # double underscore (__) before variable make it private.

    def getBalance(self):
        return self.__balance

    """ Deposit Method """
    def deposit(self, amount):
        if 0 < amount:
            self.__balance += amount 
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid amount!")

    """ Withdraw Method """
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount 
            print(f"{amount} withdrawn successfully!")
        else:
            print("Invalid amount!")

if __name__=="__main__":
    acc = BankAccount(10000)
    print(f"Current Balance: {acc.getBalance()}")
    acc.deposit(3000)
    print(f"After deposit 3000")
    print(f"Current Balance: {acc.getBalance()}")
    acc.withdraw(7000)
    print(f"After withdraw 7000")
    print(f"Current Balance: {acc.getBalance()}")

