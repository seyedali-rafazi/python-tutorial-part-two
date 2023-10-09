import json
from pathlib import Path


users = [
    {"id" : 1 , "name" : "ali" , "age" : 23},
    {"id" : 2 , "name" : "ali" , "age" : 23},
    {"id" : 3 , "name" : "ali" , "age" : 23},
    {"id" : 4 , "name" : "ali" , "age" : 23},
    {"id" : 5 , "name" : "ali" , "age" : 23},
    {"id" : 6 , "name" : "ali" , "age" : 23},
    {"id" : 7 , "name" : "ali" , "age" : 23},
    {"id" : 8 , "name" : "ali" , "age" : 23}
]

data = json.dumps(users)
Path("data.json").write_text(data)