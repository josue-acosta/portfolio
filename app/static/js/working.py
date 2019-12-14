import json
import os

json_file_path = "rates.json"

with open(json_file_path, 'r') as j:
     food_object  = json.loads(j.read())

for food_item in food_object:
    print(food_item)
