items = [
    ("product2005", 10),
    ("product2002", 16),
    ("product200", 1),
    ("product2003", 70)
]

filtered = list((filter(lambda item: item[1] >= 10, items)))
print(filtered)
