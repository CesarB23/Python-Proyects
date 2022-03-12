# A tuple is a collection data type that is ordered but cant be modified

mytuple = ("MAx",26,"Boston") # Can use parenthesis or not "MAx",26,"Boston"
#Can create a tuple from a list
mytuple = tuple(["MAx",26,"Boston"])
#Indexing still the same as in lists
print(mytuple)

if "Max" in mytuple:
    print("Yes")
else:
    print("No")

#Count elements in a tuple 
mytuple = ('a','b','c','c','o')
print(mytuple.count('c'))

#With index we can get de index of the first ocurrency
print(mytuple.index('o'))
#We can convert from tuple to list and viceversa, with list and tuple functions

mylist = list(mytuple)
print(mylist)
mytuple2 = tuple(mylist)
print(mytuple2)

# The colon : and doble colon :: is the same as in lists
#We can pack values in a tuple simply by ,
tuples = "max",'j',25
print(tuples)
#Unpackaging the elements is a tuple by matching to a variable
mytuple = ("Max",26,"Boston")
Name,Age,city = mytuple
print(Name)
print(Age)
print(city)
print(type(Name))
# The asterisc indicates that all the elements between i1 and i3 are located in i2 and it creates a list of them
mynumbers = (0,1,2,3,4,5)
i1,*i2,i3 = mynumbers
print(i1)
print(i3)
print(i2)

