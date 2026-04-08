# question 1
# Write a program to store seven Marks in a list entered by the user
# Marks = []
# f1 = input("Enter Marks name :")
# Marks.append(f1)
# f2 = input("Enter Marks name :")
# Marks.append(f2)
# f3 = input("Enter Marks name :")
# Marks.append(f3)
# f4 = input("Enter Marks name :")
# Marks.append(f4)
# f5 = input("Enter Marks name :")
# Marks.append(f5)
# f6 = input("Enter Marks name :")
# Marks.append(f6)
# f7 = input("Enter Marks name :")
# Marks.append(f7)
# print(Marks)
# question 2
# Write a program to accept marks of 6 students and display them in a sorted
# manner.
# Marks = []
# f1 = int(input("Enter Marks here :"))
# Marks.append(f1)
# f2 = int(input("Enter Marks here :"))
# Marks.append(f2)
# f3 = int(input("Enter Marks here :"))
# Marks.append(f3)
# f4 = int(input("Enter Marks here :"))
# Marks.append(f4)
# f5 = int(input("Enter Marks here :"))
# Marks.append(f5)
# f6 = int(input("Enter Marks here :"))
# Marks.append(f6)
# f7 = int(input("Enter Marks here :"))
# Marks.append(f7)
# Marks.sort() # this will sort the list in ascending order
# print(Marks)


# Question 3
# Check that a tuple type cannot be changed in python

# a= (1,4,56,78,45,"Salik" , True,"Raj")

# a[1] = 45 # this will give an error because tuple is immutable
# print(a)

# question 4 
# Write a program to sum a list with 4 numbers.
# li = [23,45,67,45]
# print(sum(li))

# Question 5 
#Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0,0, 9)
# c =a.count(0)
# print(c)
# print(a)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a & b)

# a = [10, 20, 30, 40, 50, 60]
# print(a[1:5:2]) # 20 , 40

# a = [1, 2, 3]
# a.append(4)
# a[1] = 10
# print(a) # 1,10,3,4

# t = (1, 2, 3)
# t[0] = 5 # this will give error because tuples are immutable

# s = {1, 2, 2, 3, 4, 4}
# print(s) #{1,2,3,4} 

# d = {"name": "Salik", "age": 21}
# print(d["name"]) # Salik 

# d = {"a": 1, "b": 2}
# d["a"] = 100
# print(d) # 100 , 2

# Task 1: Shopping Cart (List)

# 👉 Create a cart and:
# Add 3 items
# Remove 1 item
# Print final cart

# cart = ["apple" , "milk" , "bread" , "cheese"]
# cart.remove("cheese")
# print(cart)

# marks = {
#     "math": 80,
#     "science": 90,
#     "english": 70
# }
# sum = 0 
# sum = marks["math"] + marks["science"] + marks["english"]
# print(sum)

# total = sum(marks.values())
# average = total / len(marks)

# print("Total Marks:", total)
# print("Average Marks:", average)


# avg =  ( marks["math"] + marks["science"] + marks["english"]) / 3
# print(avg)


# nums = [1, 2, 2, 3, 4, 4, 5]
# unique = set(nums)
# print(unique)


# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# moive= []
# f1 = input("Enter movie name :")
# moive.append(f1)
# f2 = input("Enter movie name :")
# moive.append(f2)
# f3 = input("Enter movie name :")
# moive.append(f3)

# print(moive)


# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

# a = [1,2,3,2,1]
# a = [1,"abc" , "abc" ]
# b = a.copy()
# b.reverse()
# if a == b:
#     print("Palindrome")
# else:    print("Not Palindrome")


# WAP to count the number of students with the “A” grade in the following tuple.

t = ("A", "B", "C", "A", "D", "A", "B")
# count_a = t.count("A")
# print(count_a)

# Store the above values in a list & sort them from “A” to “D”

# grade = list(t)
# grade.sort()
# print(grade)

num =  [1,2,3,4,5,6]
i = 0 
j = len(num) -1
while i < j:
    num[i] , num[j] = num[j] , num[i]
    i += 1
    j -= 1

print(num)


