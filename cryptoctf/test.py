import json

d = {1:1, 2:2, 3:3}
s = ''

s = json.dumps(d)

print(type(s))

print(type(json.loads(s)))