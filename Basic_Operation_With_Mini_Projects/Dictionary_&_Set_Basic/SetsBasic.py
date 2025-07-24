## Sets Basic 

collection = {1,2,3,4}

print(collection)
print(type(collection))

#Empty

Student = set()

print(Student)

#Methods 

print(collection.remove(3))

print(collection.add(5))

print(collection.pop())

print(collection.clear())


## Union and Intersection

set1 = {1, 2, 3}
set2 = {3, 2 , 4}

print(set1.union(set2))

print(set1.intersection(set2))