from sys import getsizeof

values = (x*2 for x in range(1000))
list = [x*2 for x in range(1000)]

print("generator:", getsizeof(values))
print("list:", getsizeof(list))

