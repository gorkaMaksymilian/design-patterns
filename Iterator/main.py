from Collection import Collection

array_collection = Collection([0,0,4,3,0,2,0,6,7,4,0,0])

simple_iterator = array_collection.iterator()
for item in simple_iterator:
    print(item,end=" ")
print()

non_zero_iterator = array_collection.non_zero_iterator()
for item in non_zero_iterator:
    print(item,end=" ")
