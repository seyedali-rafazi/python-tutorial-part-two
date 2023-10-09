items = [
    ("product2005", 10),
    ("product2002", 16),
    ("product200", 1),
    ("product2003", 70)
]


# prices = list(map(lambda item: item[1]   , items))
prices = sorted([item[1] for item in items])

filtered = list((filter(lambda item: item[1] >= 10, items)))
filtered = [item[1] for item in items if item[1] >= 10]

print(prices)
print(filtered)

