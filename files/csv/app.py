import csv

#with open("date.csv" , "w" , newline="") as file:
#    writer = csv.writer(file)
#    writer.writerow(["id" , "name" , "phone"])
#    writer.writerow(["1" , "ali" , "333"])
#    writer.writerow(["2" , "mahdi" , "444"])
#    writer.writerow(["3" , "ehsan" , "555"])
#    writer.writerow(["4" , "reza" , "666"])
    
    
with open("date.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)