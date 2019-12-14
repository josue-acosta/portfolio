import json

json_file_path = "rates.json"

with open(json_file_path, 'r') as j:
     state_of_good_repair  = json.loads(j.read())
    
table_columns = state_of_good_repair["meta"]["view"]["columns"]

for column in table_columns:
    if column["id"] > 0:
        print("name: " + column["name"])
        print("description: " + column["description"])

        if len(column["cachedContents"]):
            for item in column["cachedContents"]["top"]:
                print(item["count"])

    
