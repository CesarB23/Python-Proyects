mylst = [1,2,3,4,5,6,7,8,9]
# start-end point by colon, no star point indicates starts from 0 as well for the end
a = mylst[0:5]

print(a)

# Two colons indicate a step and a start point, also accepts negativa index
b = mylst[0::2]
print(b)
# A nice way to reverse a list, 
b = mylst[::-1]
print(b)

list_org = ["Banana", "cherry","Apple"]
#Another option with the list function
list_copy = list(list_org)

# print(list_copy)
# print(list_org)

# list_copy = list_org[:]
# list_copy.append("Coliflower")
# list_copy = list_org.copy()
# list_copy.append("Wea")
# print(list_copy)
# print(list_org)

mylst = [1,2,3,4,5,6,7,8,9]
b = [i*i for i in mylst]
print(mylst)
print(b)

cow = []
for element in mylst:
    e = element*element
    cow.append(e)
print(cow)
# Zip function to concatenate elements from lists to a tuple
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i for i, in zip(list1)]
print(list3)

# Loops for x,y in 2 lists to concatenate
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [x + y for x in list1 for y in list2] #00 , 01, 10,11 iterations
print(list3)
# 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

aList = ['a', 'b', 'c', 'd']

newlist.copy(aList)

newlist = list(aList)
print(newlist)

newlist2 = newlist.copy()
print(newlist2)
aList = [5, 10, 15, 25]
print(aList[::-1])
print(aList[::-2])

