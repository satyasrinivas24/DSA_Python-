#-------------------classes-object python------------------------------------------------------------------------------------
class Bankaccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance +=amount
        print(f"{amount} is deposited.New balance is {self.balance}")
        
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient amount")
        else:
            self.balance -=amount
            print(f"{amount} is withdraw.New balance is {self.balance}")
        
    def get_balance(self):
        return self.balance
    
bank = Bankaccount("srinu",2000)
print(bank.balance)
bank.deposit(2000)
bank.withdraw(2700)
print(bank.get_balance())