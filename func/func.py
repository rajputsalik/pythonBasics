
# # def goodDay(name):
# #    print(f"Good day to you, {name}")

# # goodDay("Mohd Salik")    


# username = "Mohd Salik"
# def func():
#    username = "chai"
#    print(username)


# print(username)   
# func()


# x= 99 

# def func2(y):
#    z = x + y
#    return z

# result = func2(1)
# print(result)

# def f1():
#    x = 88
#    def f2():
#        print(x)
#    f2()

# f1()


# def add(*arg):
#    total = 0
#    for i in arg:
#       total+=i

#    return total   


# def add(*arg):
#     return sum(arg)
      

# result = add(4,2,4,5)
# print(result)


# def person(name = "john" , age=18):
#     print("name :" ,name)
#     print("age :" ,age)

# person(30,'salik') 


# def person(**kwargs):
#    print(kwargs)

# person(age = 30, name = 'salik' , loc = 'ahmedabad' , tech = 'python') 


# def demo(a,*args , **kwargs):
#    print('a : ' ,a)
#    print('args : ' , args)
#    print('kwargs : ' , kwargs)


# demo(10 , 20,30,40,50,60, name='salik' , age = 18, loc = 'ahmedabad' , tech = 'python' )


# def square(num):
#     return num * num 

# def cube(num):
#     return num * num  * num

# def high_order_function(nums ,high):
#       for i in nums:
#            result = high(i)
#            print(result)


# value =[5,6,7]
# high_order_function(value , square)


# def inp():
#     num = int(input("Enter how many numbers"))
#     print(f"enter a number {num} times")
#     numbers = []
#     for _ in range(num):
#         list= int(input("Enter a number"))
#         numbers.append(list)
#     return numbers

# def squar(nums):
#     return nums*nums

# def hof(num , high):
#     for i in num:
#         result = high(i)
#         print(result)


# a = inp()
# hof(a,squar)    

# fun = lambda num : num * num 
# result = fun(5)
# print(result)


# add = lambda a,b : a+b 
# result = add(5,5)
# print(result)

# num = int(input("Enter a number"))

# even = lambda num : 'Even' if num% 2==0 else 'odd'
# print(even(num))


# def even(num):
#     if num% 2 ==0:
#         print('even')
#     else:
#         print('odd')

# num = 33
# even(num)        
    

def outer():
    print("In outer function")

    def inner(num):
        print("In Inner function" , num)

    return inner

something = outer()

something("salik")