tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
# checking whether item 50 exists in tuple
print(50 in tuple1)
# Output True
print(500 in tuple1)
# Output False

#Delete will delete the entire tuple
sampletup1 =(0,1,2,3,4,5,6,7,8,9,10)
del sampletup1

print(sampletup1)
# Count method to count the elements in a tuple
tuple1 = (10, 20, 60, 30, 60, 40, 60)

count = tuple1.count(60)
print(count)


count = tuple1.count(600)
print(count)


nested_tuple = ((20, 40, 60), (10, 30, 50), "Python")

# access the first item of the third tuple
print(nested_tuple[2][0])  # P

# iterate a nested tuple
for i in nested_tuple:
    print("tuple", i, "elements")
    for j in i:
        print(j, end=", ")
    print("\n")


import itertools

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

# using itertools
tuple3 = tuple(item for item in itertools.chain(tuple1, tuple2))
print(tuple3)
# Output (1, 2, 3, 4, 5, 3, 4, 5, 6, 7)


tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])+

tuple50 = (50,)
print(tuple50)

tuple1 = (10, 20, 30, 40)

t1,t2,t3,t4 = tuple1
print(t1,t2,t3,t4)

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1,tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

tuple1 = (11, 22, 33, 44, 55, 66)

t1 ,t2 = tuple1[3:5]
print(t1,t2)
tuple2= t1,t2
print(tuple2)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

tuple1 = (45, 45, 45, 45)
print(all(tuple1))

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
s = []
newtuple = ()
for n,t in tuple1:
    print(n,t)
    s.append(t)   
s.sort()
print(s)
for i in s:
    print(i)
    for x,y in tuple1:
        print(x,y)
        if i == y:
            newtuple += (x,y)
    print(newtuple)