# question 1
# Store following word meanings in a python dictionary

# dict ={
#     'table' : ["a piece of furniture" , "list of facts & figures"] ,
#     'cat' : "a small animal"
# }

# print(dict)

# question 2

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.

# subject = {
#     "python","java","C++","python","javascript","java","python","java","C++","C"
# }

# print(subject)
# print(len(subject) , "classrooms needed")

# Question 3

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

# marks = {}
# name = input("enter a name of the subject :")
# marks[name] = int(input("enter marks :"))

# name = input("enter a name of the subject :")
# marks[name] = int(input("enter marks :"))

# name = input("enter a name of the subject :")
# marks[name] = int(input("enter marks :"))

# print(marks)

# question 4

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

# st = {9,"9.0"}
# print(list(st))

# question 5 
# Write a program to create a dictionary of Hindi words with values as their English

dic = {
    "dil" : "heart" ,
    "darvaza" : "door" ,
    "duniya" : "world"
}

word = input("enter a Hindi word :")
print(dic.get(word , "word not found in dictionary")) # this will return the value of the key 'word' if it is present in the dictionary, otherwise it will return "word not found in dictionary"

# print(dic)

# question 6
# Write a program to input eight numbers from the user and display all the unique
# numbers (once)
# num = set()
# num.add(int(input("enter a number :")))
# num.add(int(input("enter a number :")))
# num.add(int(input("enter a number :")))
# num.add(int(input("enter a number :")))
# num.add(int(input("enter a number :")))
# num.add(int(input("enter a number :")))
# num.add(int(input("enter a number :")))
# num.add(int(input("enter a number :")))
# print(num)

# question 7
# Can we have a set with 18 (int) and '18' (str) as a value in it?
# solution  = {18 , "18"} # yes we can have both int and str in a set because they are different data types
# print(solution)

# question 8
#  What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations? is 2 because 20 and 20.0 are considered the same in python as they are both numbers and have the same value, while '20' is a string and is different from the number 20.
# print(len(s)) 

# question 9 

# What is the type of 's'?
# s = {} # it will be dictinoary because {} is used to make empty set we have to use set() 

# question 10

# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# dict = {}
# name = input("enter your name :")
# dict[name] = input("enter your favorite language :")

# name = input("enter your name :")
# dict[name] = input("enter your favorite language :")

# name = input("enter your name :")
# dict[name] = input("enter your favorite language :")

# name = input("enter your name :")
# dict[name] = input("enter your favorite language :")

# print(dict)

# question 11
# If the names of 2 friends are same; what will happen to the program in problem
# 6? it wil overwrite the pervious value of the key with the new value because in a dictationary keys are unique 

# question 12 
# Can you change the values inside a list which is contained in set S

# s = {8, 7, 12, "Harry",[1,2]} # this will give an error because list is mutable and set is immutable so we cannot have a mutable data type inside a set 