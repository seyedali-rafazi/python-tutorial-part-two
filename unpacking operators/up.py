first = [1,2,3,4]
second = [4,6,7,8]

Values = [*first , 4 , *second , *"Hello" , *range(10)]
print(Values)
print(*Values)

x_val = {"x":10 , "y":43}
y_val = {"x":20 }

combined = {**x_val , **y_val}
print(combined)

