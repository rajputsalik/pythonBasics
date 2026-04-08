# class Studemt:
#     name = "Mohd Salik"

# s1 = Studemt()
# print(s1.name)


# class Students:

#     def __init__(self , fullname , age , grade):
#         self.name = fullname
#         self.age = age
#         self.grade = grade
#         print("Student is created")

# s1 = Students("Mohd Salik", 22 , "A")
# print(f"Name :{s1.name}")
# print(f"Age :{s1.age}")
# print(f"Grade :{s1.grade}")

# s2 = Students("Mohd Saqib", 19, "A")
# print(f"Name :{s2.name}")
# print(f"Age :{s2.age}")
# print(f"Grade :{s2.grade}")



# class Studemt:
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         return round(sum(self.marks) / len(self.marks),2)

# s1 = Studemt("Mohd Salik" , [78,98,90])
# print(s1.name + " has marks " + str(s1.marks) + " and average is " + str(s1.get_avg()))
# # print(f"Average Marks : {s1.get_avg()}")

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#          self.acc = True
#          self.brk = False
#          self.clutch = False
#          print("Car is started")


# car1 = Car()
# car1.start()

# class Account:
#     def __init__(self , bal , acc):
#         self.balance = bal
#         self.account = acc

#     def debit(self , amount):
#         self.balance -= amount
#         print(f"RS {amount} is debited from your account {self.account}")
#         print(f"Your current balance is {self.get_balance()}")

#     def credit(self , amount):
#         self.balance += amount
#         print(f"RS {amount} is credited to your account {self.account}")
#         print(f"Your current balance is {self.get_balance()}")    


#     def get_balance(self):
#         return self.balance    


# acc1 = Account(10000 , 12345)
# acc1.debit(5000)
# acc1.credit(2000)
# acc1.debit(4000)
# acc1.credit(2000)

# acc1.credit(300000)

# class Car:
#     def __init__(self , brand , model):
#         self.brand = brand
#         self.mdel=model

# my_new_car = Car("Tata" , "Safari")
# print(my_new_car.brand)
# print(my_new_car.mdel)



# class Car:
    
#     def __init__(self , type):
#        self.type = type

#     @staticmethod
#     def start():
#         print("Car Start. ") 

#     @staticmethod
#     def stop():
#         print("Car Stopped. ")   

# class ToyotaCar(Car):
#     def __init__(self , name , type):
#         super().__init__(type)
#         self.brand = name
#         super().start()

        
# car1 = ToyotaCar("fortuner" , "Petrol")

# print(car1.type)



# class A:
#     varA =  "welcome to class A"

# class B:
#      varB =  "welcome to class B"

# class C(A,B):
#       varc =  "welcome to class c"

# c1 = C()     
# print(c1.varA)
# print(c1.varB) 
# print(c1.varc)



        
# class computer:
#     def config(self):
#         print("17 , 16GB , 1Tb")

# com1 = computer()
# com2 = computer()

# computer.config(com1)

# com1.config()


# class laptop:
#     def details(self , brand , ram):
#         self.brand = brand 
#         self.ram = ram
#         print(brand , ram)

# lap1 = laptop()
# lap2 = laptop()
# lap1.details("Dell" , "16GB")
# lap2.details("Hp" , "64GB")


 
class Device:
    def __init__(self , name):
        print("Init called for" , name)
        self.name = name.upper()

    def show(self):
        print("Device: " , self.name)

d1 = Device("laptop")
d2 = Device("mobile")

d1.show()
d2.show()





    
