from timeit import timeit

code1 = """
def age_calculater(age):
    if age <= 0:
        raise ValueError("Age can not be 0")
    return 10 / age

try:
    age_calculater(-1)
except ValueError as ex:
    pass
"""


code2 = """
def age_calculater(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = age_calculater(-1)
if xfactor == None:
    pass
"""


print(timeit(code1, number=10000))
print(timeit(code2, number=10000))
