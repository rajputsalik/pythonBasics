# friend = ["Salik","Raj" , "Apple" , "Mango" , "Orange" , 5,45.06 , False]
# print(friend)

# friend.append("banana")
# print(friend)

# l1 = [32,45,3,2,78,32,45,67,89]
# l1.sort() # this will sort the list in ascending order
# l1.reverse() # this will reverse the list
# l1.insert(2,100) # this will insert 100 at index 2 and shift the rest of the elements to the right
# l1.remove(45) # this will remove the first occurrence of 45
# print(l1.count(45)) # this will count the number of occurrences of 45 in the list
# print(l1.copy()) # this is a shallow copy of list
#l1.pop(2) # this will remove the element at index 2

# print(l1)


# list comprehension is a concise way to create lists. 
# It consists of brackets containing an expression followed by 
# a for clause, then zero or more for or if clauses. 
# The expressions can be anything, meaning you can put 
# in all kinds of objects in lists.


# list = [[1,2,3],[4,5,6],[7,8,9]]
# flattend_list = [item for sublist in list for item in sublist]
# print(flattend_list)

# list = [1,2,3,4,5,6,7,8,9]
# even = [item for item in list if item%2==0]
# print(even)

# list = [1,2,3,4,5,6,7,8,9]
# sq = [item**2 for item in list]
# print(sq)

# list = ["Salik" , "Raj" , "Rohit" , "Suresh" , "Anil"]
# letter = [item[0] for item in list]
# print(letter)


# list = [1,2,3,4,5,6,7,8,9]
# even_square = [item**2 for item in list if item %2==0]
# print(even_square)

# list = [1,2,3,4,5,6,7,8,9]
# int_to_string = [str(item) for item in list]
# print(int_to_string)
# print(type(int_to_string[5]))


# list = ["1","2","3","4","5","6","7","8","9"]
# string_to_int = [int(item) for item in list]
# print(string_to_int)
# print(type(string_to_int[5]))


# num = int(input("enter a number :"))

# for i in range(2,num):
#     if num%i==0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")


# num = int(input("enter a number :"))


a= 3
b=4
a,b = b,a #this called unpacking and packing of variables, this will swap the values of a and b without using a temporary variable
print(a,b)

even= [x for x in range(10) if x%2==0 ]
print(even)

add = lambda a,b : a+b
print(add(10,12))

sq = lambda a : a**2 
print(sq(4))