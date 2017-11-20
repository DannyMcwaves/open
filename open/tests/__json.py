from open import Json
from open import JSON_DATA, JSON_DATA2

json = Json(JSON_DATA)
print(json)
print(type(json.json_read_file))
print(len(json))
for i in json:
    print(i['_id'])

print('\n---------------\n')

json2 = Json(JSON_DATA2)
print(json2)
print(type(json2.json_read_file))
print(len(json2))
for key in json2:
    print(key['city'])
