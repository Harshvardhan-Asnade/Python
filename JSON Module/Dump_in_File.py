import json

data = {"name": "Harsh", "age": 20}

with open("data.json", "w") as file:
    json.dump(data, file)