import json
from pathlib import Path


data = Path("data.json").read_text()
print(data)
print(type(data))


users = json.loads(data)
print(type(users))

