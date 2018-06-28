import pymongo
#链接mongodb  数据库
client = pymongo.MongoClient(host = 'localhost',port=27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client.test
db = client['test']
collection = db.students


student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
result = collection.insert(student)
print(result)