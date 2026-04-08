# class Laptop:
#    def build(self):
#       print("Laptop bulids")

# class Desktop:
#    def build(self):
#       print("Desktop bulids")

# class Alien:
#    def code(self , machine : Laptop):
#       print("Alien Bulding..")
#       machine.build()

# assus = Laptop()
# beast = Desktop()
# salik = Alien()

# salik.code(beast)

 
class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        print("B show")
        super().show()

obj = B()
obj.show()