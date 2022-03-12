#its a collection data type that is mutable, unordered and dont accept duplicates 
myset = {5,3,4,5,}
print(myset)
#can be created with the set function, accepts an list as an input
myset = set("Coñe")
print(myset)

#To create an empty set we use the built in set method not the  empty {}
newset = set() 
print(newset)
# We can add new elements to the set
newset.add(1)
newset.add(2)
newset.add(3)
print(newset)
#also we can remove them, also the .discard() works
newset.remove(3)
print(newset)
# We can use the .clear() method to remove the set
#Also the .pop() method is helpfull for eliminate an arbritary element in the set
print(newset.pop())
print(newset)
#loops still the same
for i in newset:
    print(i)
#As well as checking for an specific item in a set
if 1 in newset:
    print("Yes")