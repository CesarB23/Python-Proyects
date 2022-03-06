#Lists: Is a collection data type that is ordered, mutable and allow us to duplicate elements

from numpy import iterable


lst = ["banana","cherry","apple"]
print(lst)

lst2 = list() # Method to create a list
print(lst2)

lst3 = [5,True,'apple'] #Accepts every type of data, repeted 
print(lst3)

#List indexing [n] value of the list

item = lst[0] # [-1] is the last value and so on
print(item)

for list in lst: # loop through the list positions
    print(list)

print(len(lst)) # Lenght of a list

if "banana" in lst: # Checks if an item is a list
    print("yes")
else:
    print("no")

lst.append("lemmon") # Append an object at the end of the list
print(lst)

lst.insert(2,"Cucumber") # Inserts a item at an specific position in the list
print(lst)

item = lst.pop() # Remove the last element of a list
print(item)
print(lst)

item = lst.remove("apple") # Removes an specific item from the list
print(lst)

item = lst.clear() # Clear the whole list
print(lst)

lst = ["banana","cherry","apple"]

item = lst.reverse() # Reverse the elements in a list
print(lst)

item = lst.sort() # sort values from biggest to smaller
print(lst)

lst = [-1,2,5,9,10,0] 
print(lst)
item = lst.sort() # sorts the list but modifies it
print(lst)

lst = [-1,2,5,9,10,0] 
print(lst)
nlst = sorted(lst) # Creates a new sorted list without modifying the original
print(lst)
print(nlst)

num = [0] *5 # creates a list of ceros
print(num)

num2 = [1,2,3,4,5]
print(num2)

num3 = num + num2 # Append 2 lists 
print(num3)