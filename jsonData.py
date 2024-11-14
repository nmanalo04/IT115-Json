#import thr syntac in this code
import json

#created the dictionary fpr hits block of code

data1 = {
    'name':'Nikaya Manalo',
    'age':26,
    'city':'Seattle',
    'interest': ['Hiking','Videogames','Paddle Boarding','Travel'],
    'is_student': True
}

#we wrote the json file on this block of code
#we created a folder for data.json
with open('data1.json', 'w') as file:
    #dump the data dictionary into the Json file
    json.dump(data1, file, indent=4)

print("data has been written into data1")
#Read the JSON file.

with open("data1.json", "r") as json_file:
    loaded_data = json.load(json_file) 

print("Successfully able to read data1.json")
print(loaded_data)


#change the contents of the JSON dictionary

loaded_data['age'] = 27
loaded_data['interest'].append('Gym')


#loaded_data['interest'].remove()
#resave the altered json file

with open('data2.json', 'w') as file:
        json.dump(loaded_data, file, indent=4)

print('Modified')
print(loaded_data)