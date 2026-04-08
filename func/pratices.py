# 1.Write a program using functions to find greatest of three numbers.
# def greatest(a,b,c):
#     if(a>=b and a>=c):
#         print(f"{a} is gratest number")
#     elif(b>=a and b>=c):
#         print(f"{b} is gratest number")
#     else: 
#         print(f"{c} is gratest number")
#     return greatest        

# a = int(input("enter a number :"))
# b = int(input("enter a number :"))
# c = int(input("enter a number :"))
# greatest(a,b,c)


# 2. Write a python program using function to convert Celsius to Fahrenhei t.
# def fahrenheit(Celsius):
#     fah = (Celsius *9/5) + 32
#     return fah

# Celsius = float(input("Enter temperature in Celsius: "))
# print(f"{Celsius} degree Celsius is equal to {fahrenheit(Celsius)} degree Fahrenheit.")


# 3. How do you prevent a python print() function to print a new line at the end.

# print("Hello" , end=" ")

# 4. Write a recursive function to calculate the sum of first n natural numbers.

# def sum_natural(n):
#     if n==1:
#         return 1
#     return sum_natural(n-1) + n 

# print(sum_natural(4))


# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

# def pattern(n):
#     if(n==0):
#         return
#     pattern(n-1)
#     print("*" * n)

# pattern(5)


# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# print("\n")
# pattern(5)



# 6. Write a python function which converts inches to cms.

# def in_to_cm(inches):
#     cm = inches*2.54
#     return cm

# print(in_to_cm(10))

# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.

# def remove_word(word, lst):
#     l = []
#     for item in lst:
#         if not(item == word):
#             l.append(item.strip(word))
#     return l

# lst = ["apple" , "banana" , "grapes" , "orange"]
# print(remove_word("a", lst))
# # 8. Write a python function to print multiplication table of a given number.

# def mult(a):
#     for i in range(1,11):
#         print(f"{a} * {i} = {a*i}")
#     return mult

# n = int(input("enter a number :"))
# mult(n)



