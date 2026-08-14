""" Custom Error """
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Not enough balance!")
        self.__balance -= amount
        print(f"Withrawn: {amount}\nCurrent balance: {self.__balance}")
        
    def getBalance(self):
        return self.__balance
 
       
if __name__=="__main__":
    try:
        acc = BankAccount(10000.00)
        print(f"Balance: {acc.getBalance()}")
        acc.withdraw(10000.20)
    except InsufficientBalanceError as e:
        print(f"ERROR: {e}")
    finally:
        print("Program executed...")