
try :
    with open("exception/content.txt") as file , open("target.txt" , "x") as target:
       print("file opend")
    age =  int(input("Age: "))
    print("test")
    print(10 / age)
except (ValueError , ZeroDivisionError):
    print("it is unvalid input")
else:
    print("No exeption")
  
        
print("Done")