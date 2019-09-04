# -*- coding: utf-8 -*-
import redis


class Base:

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)


class TestString(Base):
    """
    set
    get
    mset
    mget
    """

    def test_set(self):
        result = self.r.set('name', 'Amy')
        return result

    def test_get(self):
        result = self.r.get('name')
        return result

    def test_mset(self):
        d = {
            'name1': 'Bob',
            'name2': 'Bob2'
        }
        result = self.r.mset(d)
        return result

    def test_mget(self):
        l = ['name', 'name1', 'name2']
        result = self.r.mget(l)
        return result

    def test_del(self):
        result = self.r.delete('name2')
        return result


class TestList(Base):

    def test_push(self):
        # lpush/rpush 从左/右插入数据
        t = ('Amy', 'Jhon')
        t = ['Amy', 'Jhon']
        result = self.r.lpush('l_eat', *t)
        rest = self.r.lrange('l_eat', 0, -1)
        print(rest)
        return result

    def test_pop(self):
        # lpop/rpop 移除最左/最右的元素并返回
        rest = self.r.lpop("l_eat")
        print(rest)
        rest = self.r.lrange("l_eat", 0, -1)
        print(rest)


class TestSet(Base):
    def test_sadd(self):
        # sadd 添加元素
        l = ['Cat', 'Dog']
        rest = self.r.sadd('zoo2', *l)
        print(rest)
        rest = self.r.smembers("zoo2")
        print(rest)

    def test_srem(self):
        # srem 删除元素
        rest = self.r.srem('zoo1', "Dog")
        print(rest)
        rest = self.r.smembers("zoo1")
        print(rest)

    def test_sinter(self):
        # 交集
        rest = self.r.sinter('zoo1', 'zoo2')
        print(rest)


def main():
    # str_obj = TestString()
    # str_obj.test_set()
    # r = str_obj.test_mset()
    # r = str_obj.test_mget()
    # r = str_obj.test_del()
    # list_obj = TestList()
    # r = list_obj.test_push()
    # print(r)
    # list_obj.test_pop()
    set_obj = TestSet()
    # set_obj.test_sadd()
    # set_obj.test_srem()
    set_obj.test_sinter()


if __name__ == '__main__':
    main()
