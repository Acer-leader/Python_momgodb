#写入文件
import csv
#写入 'w'    #追加写入'a'           存储的数据之间要加什么 用 delimiter=''  该参数
with open('data.csv','w') as file:
    writer = csv.writer(file,delimiter=' ')
    writer.writerow(['id','name','age'])
    writer.writerow(['1','mike','13'])
    writer.writerow(['2','bob','12'])
    writer.writerows([['3','bb','14'],['4','www','54']])

with open('data1.csv', 'w') as file:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
print('======================')
import csv
# 读取数据
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
