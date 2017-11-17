from open.main.json import Json
from open.main.variables import JSON_DATA

json = Json(JSON_DATA)

print(json)
print(json.json_read_file['_id'])
print(json.json_read_file.keys())
for key, value in json.json_read_file.items():
    print(key, value)
