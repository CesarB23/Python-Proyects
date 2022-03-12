# a dictionary is a collection data type that is orderend, mutalbel, consists of  key-value pair

mydict = {"name": "Max","age":28,"city":"New York"}
print(mydict)
#We can create them by the dictionary built in function
mydict2 = dict(name="Kobe",age=30,city="Los Angeles")
print(mydict2)
#Accesing the values, by indexing with the key
print(mydict["name"])
#Because it mutable, we can append new key-value pairs
mydict["email"] = "max@gmail.com"
print(mydict)
#del statment delets key-value pairs
del mydict["name"] 
print(mydict) 
#also with the pop method, popitem removes the last item from the dict
mydict.pop("age")
print(mydict)
#Check if exists a key-value pair in a dict
if "name" in mydict:
    print(mydict["name"])
else:
    print("Error")

try:
    print(mydict["city"])
except:
    print("Error")
# We cam loop thru key, values or both in the same loop
for key in mydict.keys():
    print(key)
for values in mydict.values():
    print(values)
for key,values in mydict.items():
    print(key,values)
#This creates a copy of the original dict but, modifying the copy affects the original
mydict_copy = mydict
print(mydict_copy)
#The .copy() function should be used in order to make a real copy
mydict_copy = mydict.copy()
print(mydict_copy)
#Also by the dict function itself
mydict_copy = dict(mydict)
print(mydict_copy)
#We can update a dictionary with another values with the .update() function
my_dict1 = {"name":"Xokas","Age":26,"City":"Madrid"}
my_dict2 = dict(name="Pedro",email="pedro@gmail.com")
#Also we can append new key-value pairs
my_dict1.update(my_dict2)
print(my_dict1)
#When we use numbers as a key, in order to use indexing we should refer to that specific number key, not the position
dictnumbers = {3:9,4:16,5:25}
print(dictnumbers[3])