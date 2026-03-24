# Type of inheritance
# 1. Single Level Inheritance
# 2. multi lEvel Inheritance

# Base class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")


# Single + Hierarchical
class SavingsAccount(BankAccount):   # Single inheritance
    def interest(self):
        print("Savings account earns interest")


class CurrentAccount(BankAccount):  # Hierarchical inheritance
    def overdraft(self):
        print("Current account allows overdraft")


# Multilevel
class PremiumSavings(SavingsAccount):   # BankAccount → SavingsAccount → PremiumSavings
    def premium_benefits(self):
        print("Premium savings has extra benefits")


# Multiple + Hybrid
class BusinessAccount(SavingsAccount, CurrentAccount):   # Multiple inheritance
    def business_feature(self):
        print("Business account has special features")


# Object
b = BusinessAccount("Harsh", 50000)

b.show_balance()     # from BankAccount
b.interest()         # from SavingsAccount
b.overdraft()        # from CurrentAccount
b.business_feature() # own method