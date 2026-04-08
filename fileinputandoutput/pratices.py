# Create a new file “practice.txt” using python. Add the following data in it:

# 1. WAF that replace all occurrences of “java” with “python” in above file. 

# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\I\\O\\practice.txt", "r") as f:
#     data =f.read()
#     new_data = data.replace("Java" , "Python")
#     print(new_data)


# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\I\\O\\practice.txt", "w") as f:
#     f.write(new_data)

# 2. Search if the word “learning” exists in the file or not.
# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\I\\O\\practice.txt", "r") as f:
#     data = f.read()
#     if "learning" in data:
#         print("The word 'learning' exists in the file.")
#     else:
#         print("The word 'learning 'does not exists in the file.")

# WAp to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

# def check_for_line():
  
#     with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\I\\O\\practice.txt", "r") as f:
#             line = f.readlines()
#             word = "programming"
#             found = False
#             for i in range(len(line)):
#                 if word in line[i]:
#                     print(f"The word {word} occurs first in line {i+1}.")
#                     found = True
#                     break

#     return -1

# check_for_line()


# From a file containing numbers separated by comma, print the count of even numbers.

# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\I\\O\\practices.txt", "r") as f:
#      data = f.read()
#      print(type(data))
#      number = data.split(",")
#      count = 0
#      for i in number:
#           if int(i)%2==0:
#                print(i)
#                count+=1

# print(f"The count of even numbers is {count}.")


# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\poems.txt", "w") as f:
#     f.write("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are!")

# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\poems.txt", "r") as f:
#     data = f.read()
#     if 'Twinkle' in data:
#         print("The word 'Twinkle' exists in the given file.")
#     else:
#             print("The word 'Twinkle' does not exist in the given file.")



# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.


# import random 

# def game():
#     print("You are playing the game...")
#     score = random.randint(1,100)
    
#     with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\hiscore.txt", "r") as f:
#             hiscore = f.read()
#             if hiscore =="":
#                   hiscore = 0
#             else:
#                   hiscore = int(hiscore)

#     print(f"Your high score is {score}")
#     if(score  > hiscore):
#           with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\hiscore.txt", "w") as f:
#                 f.write(str(score))
  
#     return score


# game()


# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.


# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} x {i} = {n*i}\n" 
        
#     with open(f"C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\tables\\table_of_{n}.txt", "w") as f:
#         f.write(table)


# for i in range(2,51):
#     generateTable(i)

# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 
# word = "donkey"
# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\donkey.txt", "r") as f:
#     data = f.read()

# new_data = data.replace(word , "######")

# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\donkey.txt", "w") as f:    
#      f.write(new_data)  
    


import json

# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\pra.json","r") as f:
#     data = json.load(f)

# print(data["name"])

# data = {
#     "Name" : "Saqib" , 
#     "Age" : 20
# }

# with open("C:\\Users\\DELL SSD\\OneDrive\\Desktop\\Python Basics\\py basics\\fileinputandoutput\\pra.json" , "w") as f:
#     data = json.dump(data , f , indent=4)

# json_string = '{"name": "Saqib"}'
# data = json.loads(json_string)


# data = json.dump(data)

lst  = [1,2,34,5]
for lis in lst:
    print(lis)



    