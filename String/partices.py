# question 1
# Write a python program to display a user entered name followed by Good Afternoon using input() function.
# name  = input("Enter a name : ")
# print("Good Afternoon, : " + name)

# question 2

# Write a program to fill in a letter template given below with name and date
# letter = '''Dear <|Name|>,
# You are selected!
# <Date>'''

# print(letter.replace("<|Name|>", "Mohd Salik").replace("<|Date|>", "20-06-2024"))

# name = input("Enter your name : ")
# date = input("enter date : ")
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)
# print(letter)

# question 3
# Write a program to detect double space in a string

# name = "my name  is Mohd salik"
# print(name.find("  "))

# question 4
# Replace the double space from problem 3 with single spaces.
name = "my name  is Mohd salik"
print(name.replace("  " , " "))

# question 5
# Write a program to format the following letter using escape sequence
# characters

letter = "Dear Harry, \n \t This python course is nice. \n Thanks!"
print(letter)