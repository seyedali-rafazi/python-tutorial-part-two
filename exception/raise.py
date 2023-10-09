def age_calculater(age):
    if age <= 0:
        raise ValueError("Age can not be 0")
    return 10 / age

try:
    age_calculater(int(input("Age: ")))
except ValueError as ex:
    print(ex)