class Account:
   def __init__(self , bal , account):
        self.bal = bal
        self.acc = account

   def credit(self ,amount):
       self.bal += amount
       print(f"RS {amount} is credit to your account {self.acc}")
       print(f"Your current balance is {self.get_balance()}")
       
   def debit(self ,amount):
       self.bal -= amount
       print(f"RS {amount} is debited from your account {self.acc}")
       print(f"Your current balance is {self.get_balance()}") 
  
   def get_balance(self):
       return self.bal
   

acc1 = Account(10000 , 12345)
acc1.debit(5000)
acc1.credit(2000)
acc1.debit(4000)
acc1.credit(2000)
  
       
       
       

