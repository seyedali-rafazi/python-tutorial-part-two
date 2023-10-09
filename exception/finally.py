
try :
    file = open("exception/content.txt")
    age =  int(input("Age: "))
    print("test")
    print(10 / age)
except (ValueError , ZeroDivisionError):
    print("it is unvalid input")
else:
    print("No exeption")
finally:
        file.close()    
        
print("Done")