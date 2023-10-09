try :
    int(input("Age: "))
    print("test")
except ValueError as ex:
    print(type(ex))
    print("it is unvalid input")
else:
    print("No exeption")
    
print("Done")