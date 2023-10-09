items = [
    ("product2005", 10),
    ("product2002", 16),
    ("product200", 1),
    ("product2003", 70)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
