items = [
    ("product2005", 10),
    ("product2002", 16),
    ("product200", 1),
    ("product2003", 70)
]

items.sort(key=lambda item: item[1])

FalaseOrTrue = list(map(lambda item: item[1] >= 10  , items))
prices = list(map(lambda item: item[1]   , items))

print(prices)
print(FalaseOrTrue)

