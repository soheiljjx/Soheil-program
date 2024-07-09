class Account:
    def __init__(self,name,number,balance,type_of_acc):
        self.name = name
        self.number = number
        self.balance = balance
        self.type_of_acc = type_of_acc
    
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        self.balance -= amount
        
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"{self.name} {self.number} {self.balance} {self.type_of_acc}"
    
name_acc1 = input("whats your name? ")
name_acc2 = input("whats your name? ")
balance_acc1 = eval(input("how much is your capital? "))
balance_acc2 = eval(input("how much is your capital? "))

acc1 = Account(name_acc1,"6037",balance_acc1,"current")
acc2 = Account(name_acc2,"6219",balance_acc2,"doposit")

print(acc1)
print(acc2)

acc1.deposit(10000)
acc2.withdraw(500)

print(acc1.get_balance())
print(acc2.get_balance())
