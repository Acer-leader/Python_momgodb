import pymysql

db = pymysql.connect(host='localhost',user='root',password='root123',port=3306,db='spiders')
cursor = db.cursor()
#新建数据
def create():
    # 建一个字典
    data =  {
        'id' : 1,
        'name': '3waa',
        'age':7233
    }
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))

    sql = 'insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
    #sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql,tuple(data.values())):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()

#更新数据

def update(age,name):
    sql = 'update students set age = %s where name = %s'
    try:
        cursor.execute(sql,(age,name))
        print('Successful')
        db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()

#删除数据
def delete():
    table = 'students'
    condition = 'age> 22'
    sql = 'delete from {table} where {condition}'.format(table=table,condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

#查询数据
def look(name):
    table = 'students'
    sql = 'select * from {table} where name = %s'. format(table=table)
    try:
        cursor.execute(sql,(name))
        print('Count:',cursor.rowcount)
        one = cursor.fetchone()
        print('One:',one)
        results = cursor.fetchall()
        print('Results:',results)
        print('Results Type',type(results))
        for row in results:
            print(row)
    except:
        print('Error')

create()

