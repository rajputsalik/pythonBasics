# Write a program to print yes when the age entered by the user is greater
# than or equal to 18.

# age = int(input("Enter your age :"))
# if age >= 18 :
#     print("yes")
# else :
#     print("No")

# question 1
# Write a program to find the greatest of four numbers entered by the user.    
# a = int(input("enter a number :"))
# b = int(input("enter a number :"))
# c = int(input("enter a number :"))
# d = int(input("enter a number :"))

# if a>=b and a>=c and a>=d :
#     print("a is greatest" , a)
# elif b>=a and b>=c and b>=d :
#     print("b is greatest" , b)
# elif c>=a and c>=b and c>=d :
#     print("c is greatest" , c)
# else :
#     print("d is greatest" , d)

# question 2
# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user

# marks1 = int(input("enter marks of subject 1 :"))
# marks2 = int(input("enter marks of subject 2 :"))
# marks3 = int(input("enter marks of subject 3 :"))

# total_percatage = (100*(marks1 + marks2 + marks3)) /300
# if  total_percatage >=40 and marks1 >=33 and  marks2 >=33  and marks3 >=33 :
#     print("Congratulations! You have passed the exam." , "Your total percentage is : " , total_percatage)
# else : 
#     print("Sorry, you have failed the exam. Better luck next time!", "Your total percentage is : " , total_percatage)

# question 3.

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# text = input("Enter a comment :")

# if "Make a lot of money" in text or "buy now" in text or "subscribe this" in text or "click this" in text :
#     print("this is a spam comment")
# else :
#     print("this is not a spam comment")


# question 4

# Write a program to find whether a given username contains less than 10
# characters or not.

# username = input("enter a name :")
# if len(username) < 10 : 
#          print("username is valid")
# else :
#     print("username is not valid")

# question 5 

# Write a program which finds out whether a given name is present in a list or not.
name = input("enter a name :")
list_of_names = ["Salik" , "Raj" , "Rohit" , "Suresh" , "Anil"]
if name in list_of_names :
    print("name is present in the list")
else :
    print("name is not present in the list")