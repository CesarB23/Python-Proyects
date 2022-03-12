
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

lis = list(filter(None,list1))
print(lis)

# Undestanding Indexing
# list1 is list, which 2 lists inside, with consecutive indexing we can access to those lists inside lists
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# print(list1[2][2][1])
# list1[2][2].append(7000)
# print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

for i in sub_list:
    list1[2][1][2].append(i)

print(list1)
#ist1[2][1][2].extend(sub_list)
# print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]
# With index we get the position of the first occurrency 
index = list1.index(20)
list1[index] = 200
print(index)
print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]
x = []
for i in list1:
    if i != 20:
        x.append(i)
print(x)

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)
