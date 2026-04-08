# # this is a decor
# def log_deco(func):
#     def wrap(*args):
#         print("Values" , args)
#         res = func(*args)
#         print("Result" , res )
#         return res 
#     return wrap



# def greater_first(func):
#     def wrap(a,b):
#         if a<b :
#             a,b = b,a
#         return func(a,b)

#     return wrap


# @log_deco 
# @greater_first
# def div(a,b):
#         return a/b
    
# result = div(2,4)
# print(result)    

# @log_deco
# def add(a,b,c):
#     return a+b+c

# result2 = add(5,6,7)
# print(result2)

# @log_deco
# @greater_first
# def sub(a,b):
#     return a-b
# result1 = sub(2,4)
# print(result1)    

list = [1,2,3,4,5,6]
x = 6
i = 0
while i < len(list):
    if  list[i] == x:
        print(f"{x}, is found at index: {i}")
        break
    else:
        i+=1
else:    
    print(f"{x}, is not found in this loop")


arr = [1,2,3,4,5]
x = 6
if x in arr:
    print(f"{x}, is found at index: {arr.index(x)}")
else:    
    print(f"{x}, is not found in this list")        