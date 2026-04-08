import requests

# def fecth_random_api():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response = requests.get(url)
#     data=response.json()
    
#     if data['success'] and "data" in data:
#         user =data["data"]
#         userName = user['login']['username']
#         country = user['location']['country']

#         return userName , country
#     else :
#         raise Exception("Failed to fech the data")
    
# def main():
#     try:
#          userNAme , country =fecth_random_api()
#          print(f"UserName: {userNAme} \ncountry:{country}")
#     except Exception as e:
#         print(str(e))

# if  __name__ == "__main__" :
#    main()           


# def fech():
#     url = "https://api.freeapi.app/api/v1/public/meals?page=1&limit=10&query"
#     respon = requests.get(url)
#     data = respon.json()

#     if data["success"] and 'data' in data:
#         recpies = data["data"]["data"]
        
#         result = []
#         for recpie in recpies:
#             recpie_name = recpie["strMeal"]
#             category = recpie["strCategory"]
#             area = recpie['strArea']
#             result.append((recpie_name , category , area))
#     return result     
    
# def main():
#     try:
#         recipes = fech()
#         for i ,(recpie_name , category , area) in enumerate(recipes , start=1):
#           print(f"The Name Of recpie is {recpie_name} \nThis repice belongs to the {area} \nAnd this repice is belongs this caegory {category}")

#     except Exception as e:
#         print("Sorry we can't load your data" , e)    

# if __name__ == "__main__":
#     main()

# import random 

# def fech():
#     url = ("https://api.freeapi.app/api/v1/public/randomjokes")
#     reponse = requests.get(url)
#     data = reponse.json()
#     # print(data)

#     if data["success"] and "data" in data:
#          jokes = data["data"]["data"]

#          if jokes:
#              randome_joke = random.choice(jokes)["content"]
#             #  print(randome_joke)
#              return randome_joke
#     return "No joke found"
    
        

# def main():
#     try:
#         joke = fech()
#         print("jokes:" , joke)
#     except Exception as e:
#         print("Sorry we can't load your data" , e)       

# if __name__ == "__main__":
#     main()




# def fech():
#     url = "https://api.freeapi.app/api/v1/public/randomjokes"
#     response = requests.get(url)
#     data = response.json()

#     if data["success"] and "data" in data:
#         jokes = data["data"]["data"]   # list of 10 jokes

#         result = []
#         for joke in jokes:
#             content = joke["content"]
#             result.append(content)

#         return result

# def main():
#     try:
#         jokes = fech()

#         for i, joke in enumerate(jokes, start=1):
#             print(f"\nJoke {i}:")
#             print(joke)

#     except Exception as e:
#         print("Sorry we can't load your data", e)

# if __name__ == "__main__":
#     main()


# def reverse_string(text):
#     reversed_text = ""
#     for char in text:
#         # Prepend character to the result string
#         reversed_text = char + reversed_text
#     return reversed_text

# # Example usage
# original = "Hello World"
# print(reverse_string(original)) # Output: dlroW olleH

complex_num = 3 + 4j
print(complex_num)



