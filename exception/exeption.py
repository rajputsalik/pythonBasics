# try:
#     a = int(input("enter a number"))  
#     b = int(input("enter a number"))  
#     result = a/b
#     print("Result is:" ,result)
# except ZeroDivisionError as e:
#     print("An error Occured" , e)
# finally:
#     print("the try and finally over ")
# print("end of execution")

# from threading import Thread

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello ",i+1)

# class Hii(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hii ",i+1)

# if __name__ == '__main__':
#     t1 = Hello()
#     t2 = Hii()

#     t1.start()
#     t2.start()


def add(a,b):
    try:
        return a+b 
    except Exception as e:
        print("this error ", e)  
    finally:
        print("code excuted")

print(add(4,4))        
