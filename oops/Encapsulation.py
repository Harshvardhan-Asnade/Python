#Wrapping data and funstions into single unit is called Encapsulation and aslo data hiding
class Bank:
    def __init__(self,AccName,AccBalance):
        self.name=AccName #public
        self.__balance=AccBalance #proteted
    def get_balance(self): #getter
        return f"{self.name} account balance is {self.__balance} Rs ."
    def set_balance(self,newbalance):#setter
        old_balance=self.__balance
        self.__balance=newbalance
        return f"{self.name} account balance has been updated from {old_balance}Rs to {self.__balance}Rs"

acc1=Bank("Harsh",100)
acc2=Bank("Ankur",200)
acc3=Bank("ajay",400)
acc4=Bank("Sai",900)
print(acc1.get_balance())
print(acc4.get_balance())
print(acc3.get_balance())
print(acc2.get_balance())

print(acc1.set_balance(100))
print(acc4.set_balance(200))
print(acc3.set_balance(300))
print(acc2.set_balance(400))

