import os
import json

json_str = '''{
    "name": "Bob", 
    "languages": ["English", "French"]
    }'''

# json str --> python dict/object (deserialization)
python_dict = json.loads(json_str)
print(f'{type(python_dict)} \n {python_dict}')

python_data = {
    "name": "Bob",
    "age": 30,
    "married": True,
    "place": "New York"
}

# python data --> json str (serialization)
json_str = json.dumps(python_data)
print(f'{type(json_str)} \n {json_str}')

DATA_FILE = 'data_file.json'
# writing python_obj in json file
with open(DATA_FILE, 'w') as write_file:
    json.dump(python_data, write_file)
print(f'{os.path.isfile(DATA_FILE)} \n data written to json file.')

# reading json file
with open(DATA_FILE, 'r') as read_file:
    print(json.load(read_file))