numbers = [1, 2, 3, 4, 5, 6]

# first , seceond , *other = numbers
# print(first , seceond , other)


first,  *other, last = numbers
print(first,  other, last)
