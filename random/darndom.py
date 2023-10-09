import random
import string

#print(random.randint(50 , 70))
#print(random.choice([2,4,5,6,7] ))
#print(random.choices([2,4,5,6,7] , k = 2))
#print(string.ascii_letters)

#print("".join(random.choices(string.ascii_letters + string.digits , k = 10)))


numbers = [1,2,3,4,5,6]
random.shuffle(numbers)
print(numbers)