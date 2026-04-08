# class A:
#     def f1(self):
#         print("f1 works")

#     def f2(self):
#         print("f2 works") 

#     def show(self):
#         print("In A show")    

# # this is single inherit 

# class B: 
#     def f3(self):
#         print("f3 works")

#     def f4(self):
#         print("f4 works")

#     def show(self):
#         print("In A show") 


# class C: 
#     def f5(self):
#         print("f5 works")

#     def f6(self):
#         print("f6 works")

#     # def show(self):
#     #     print("In A show")    

# # this is Multilevel inherit 

# class D(A,B,C): 
#     def f7(self):
#         print("f7 works")

#     def f8(self):
#         print("f8 works")

# # this is Multiple inherit 




# obj = D()
# obj.show()


class A:
    def f1(self):
        print("f1 works")
    
    def __init__(self):
        print("in A init")
   
    
# this is single inherit 

class B(A): 
    def __init__(self):
        super().__init__()
        print("in B init")


    def f2(self):
        super().f1()
        print("f2 works")


obj = B()
obj.f2()
