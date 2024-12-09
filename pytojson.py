#we are importing the json libary
import json

#we are making a json key pairs for a database

data1 = {
    "name": "Nikaya Manalo",
    "age": 23,
    "city": "Seattle",
    "intrest": ["Paddle Board", "Valorant", "Hike", "Gym"],
    "is_student": True
}

#we are making a json file in our folder and writting the above in it
with open('data1.json', 'w') as json_file:
    json.dump(data1, json_file, indent=4)

print("data has been written into data1")
#we are opening the json file and loading it into a python file
with open("data1.json", "r") as json_file:
    loaded_data = json.load(json_file) 

print("Successfully able to read file")
print(loaded_data)

#changed variables in our code like age to 30 and intrested we added being helpful
loaded_data["age"] = 30
loaded_data["intrest"].append("Being helpful")

# 

with open('data2.json', 'w') as file:
        json.dump(loaded_data, file, indent=4)
print(loaded_data)