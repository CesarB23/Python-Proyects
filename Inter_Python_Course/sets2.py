odds = {1,3,5,7}
evens = {2,4,6,8}
primes = {2,3,5,7}
# We can do union operations
U = odds.union(evens)
print(U)
#As well as Intersection
I = odds.intersection(evens)
print(I)
I = odds.intersection(primes)
print(I)
# We can calculate the difference of two setts
A = {1,2,3,4,5,6,7,8,9}
B = {1,2,3,10,11,12}
diff = A.difference(B)
print(diff)
diff = B.difference(A)
print(diff)
#Also obtain the elements that are not repeated in two sets
diff = A.symmetric_difference(B)
print(diff)
#We can do a kind of append method with .update() without duplication
A.update(B)
print(A)
#Update method, updates the data sett to the values of the operation
odds.intersection_update(evens)
print(I)
#We can use subset method as in set theory
A = {1,2,3,4,5,6}
B = {1,2,3}
C = {7,8}
print(B.issubset(A))
#superset checks if all the elements of a set are contained in the second
print(A.issuperset(B))
#isdisjoint checks if exist an null intersection in a set union
print(A.isdisjoint(C))
#The frozen set is a type of set that cant be modified or cant be used any update methods
a = frozenset([1,2,4,5,6])
print(a)




