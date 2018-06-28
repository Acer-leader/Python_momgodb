# from redis import StrictRedis
from redis import StrictRedis, ConnectionPool
# #链接redis

# redis = StrictRedis(host='localhost', port=6379, db=0, password='')
# redis.set('name','Bob')
# print(redis.get('name'))

#用 ConnectionPool   连接redis
pool = ConnectionPool(host='localhost', port=6379, db=0, password='')
redis = StrictRedis(connection_pool=pool)


#url 连接redis

# url = 'redis://:@localhost:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)
redis.set('name','Bob')
print(redis.get('name'))

