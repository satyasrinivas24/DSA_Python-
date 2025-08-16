#-------------------classes-object python------------------------------------------------------------------------------------
# class Bankaccount:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self,amount):
#         self.balance +=amount
#         print(f"{amount} is deposited.New balance is {self.balance}")
        
#     def withdraw(self,amount):
#         if self.balance < amount:
#             print("Insufficient amount")
#         else:
#             self.balance -=amount
#             print(f"{amount} is withdraw.New balance is {self.balance}")
        
#     def get_balance(self):
#         return self.balance
    
# bank = Bankaccount("srinu",2000)
# print(bank.balance)
# bank.deposit(2000)
# bank.withdraw(2700)
# print(bank.get_balance())

#--------------------------------@@ OOPS  --------------------------------------------------------------------------------------------------------
#------------------------------Inheritance-------------------------------------------------------------------------------------------
# It will take items from parent class 

# class Car:
#     def __init__(self,window,doors,engine_type):
#         self.window = window
#         self.doors = doors
#         self.engine_type= engine_type
#     def drive(self):
#         print(f"The person will be drive {self.engine_type} car")
        
# class Tesla(Car):
#     def __init__(self,window,doors,engine_type,is_selfdriving):
#         super().__init__(window,doors,engine_type)
#         self.is_selfdriving = is_selfdriving
        
#     def selfdriving(self):
#         print(f"Tesla support self driving : {self.is_selfdriving}")
    
# car = Car(4,5,'Petrol')
# car.drive()
# tesla = Tesla(4,4,'electric',True)
# tesla.selfdriving()
# tesla.drive()
    
  
#----------------   