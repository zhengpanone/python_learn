import redis
import time

# 普通连接
r = redis.StrictRedis(host='localhost', port=6379, db=0)

print(r)
'''
set(name,value,ex=None,nx=False,xx=False)
在Redis中设置值，默认，不存在则创建，存在则修改
参数：
ex，过期时间（秒）
px，过期时间（毫秒）
nx，如果设置为True，则只有name不存在时，当前set操作才执行
xx，如果设置为True，则只有name存在时，当前set操作才执行
'''

#   设置过期时间为1秒
r.set('foo', 'zone', ex=1)
# 效果同上
r.setex('foo', 'zone', 1)
# 
print(r.get('foo'))
