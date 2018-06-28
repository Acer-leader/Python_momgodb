import pymysql
db = pymysql.connect(host='localhost',user='root',password='root123',port=3306,db='spiders')
cursor = db.cursor()
#
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:',data)
# 新建数据库  spiders
# cursor.execute("create database spiders default character set utf8")
# db.close()

#创建一张表student
# sql = 'create table if not exists students (id varchar(255) not null,name varchar(255) not null, age int(60) not null,primary key (id))'
# cursor.execute(sql)
# db.close()

#插入数据

id = '20180001'
user = 'Bob'
age = 20

sql = 'insert into students(id,name,age) value (%s,%s,%s)'

try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()
