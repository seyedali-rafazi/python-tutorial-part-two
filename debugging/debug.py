def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print("Start")
print(multiply(2, 3, 4, 5, 7, 8))
