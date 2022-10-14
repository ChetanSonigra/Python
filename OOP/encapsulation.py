""" It describes the idea of wrapping data and the methods that work on data 
within one unit. This puts restrictions on accessing variables and methods
directly and can prevent the accidental modification of data. To prevent 
accidental change, an object’s variable can only be changed by an object’s method"""

# class is example of encapsulation as it combines data, methods related to one class.
# prevents accidental modification/deletion

# Access specifiers     Access from own class, access from derived class, access from object
# private member(__) :  Yes, No, No
# protected member(_) : Yes, Yes, Yes  # indicates that it is for internal use.
# public member :  Yes, Yes, Yes

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def getbalance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise Exception("amount can not be less than 0")

    def withdraw(self,amount):
        if amount > 0:
            self.__balance -= amount
        else:
            raise Exception("amount can not be less than 0")
    

acc1 = BankAccount()
print(acc1.getbalance())
acc1.deposit(100)
print(acc1.getbalance())
print(acc1.__balance)   # doesnot work
print(acc1._BankAccount__balance)  # works