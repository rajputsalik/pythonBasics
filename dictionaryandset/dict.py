dict = {
    'name' : 'salik' , 
    'age' : 21 , 
    'city' : 'Ahemdabad',
    'university' : 'RAi university' , 'data':{
        'name' : 'salik' , 
        'age' : 21 , 
        'city' : 'Ahemdabad',
        'university' : 'RAi university'
    }
}
 

info = {
    'name' : 'salik' , 
     "subjects":{
        'math' : 80 , 
        'science' : 90 , 
        'english' : 70
     }
}


# info.pop('age') # this will remove the key 'age' and its value from the dictionary
# print(info)

# info.popitem() # this will remove the last key-value pair from the dictionary
# print(info)





# print(len(list(info.keys()))) # this will return the number of keys in the dictionary
# print(list(info.values())) # this will return the number of values in the dictionary
pair = list(info.items()) # this will return the number of key-value pairs in the dictionary
print(pair[0])
print(pair[1])