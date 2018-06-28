import json
#json对象需要用双引号来包住

str = """
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]

"""
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

print(data[0]['name'])
print(data[1].get('age',25))

with open('data.json','w') as file:
    file.write(json.dumps(data,indent=2))

data = [{
    'name':'王辉',
    'gender':'男',
    'birthday':'1992-02-13'

}]
with open('data.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))

