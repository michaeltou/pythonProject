import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
json_str = json.dumps(data)
print(json_str)

d = json.loads(json_str)

print(d)
print(type(d))