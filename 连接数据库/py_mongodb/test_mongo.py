# -*- coding: utf-8 -*-
from datetime import datetime

from pymongo import MongoClient
from bson.objectid import ObjectId


class TestMongo:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def add_one(self):
        """新增数据"""
        post = {
            'title': "标题",
            "content": "内容",
            "create_data": datetime.now()
        }
        return self.db.blog.posts.insert_one(post)

    def get_one(self):
        """查询一条数据"""
        return self.db.blog.posts.find_one()

    def get_more(self):
        """查询多条数据"""
        return self.db.blog.posts.find({'title': "标题"})

    def get_one_by_oid(self, oid):
        obj = ObjectId(oid)
        return self.db.blog.posts.find_one({'_id': obj})

    def update_one(self):
        # 条件x=1,$inc 表示增加 x+10
        return self.db.blog.posts.update_one({'x': 1}, {'$inc': {'x': 10}})

    def update_more(self):
        return self.db.blog.posts.update_many({'x': 1}, {'$inc': {'x': 10}})

    def delete_one(self):
        return self.db.blog.posts.delete_one({'x': 11})

    def delete_more(self):
        return self.db.blog.posts.delete_many({'x': 11})


def main():
    obj = TestMongo()
    # result = obj.add_one()
    # print(result.inserted_id)
    # result = obj.get_one()
    # print(result['_id'])
    # result = obj.get_more()
    # for i in result:
    #     print(i["content"])
    # result = obj.get_one_by_oid("5c316b1c0b57ed373cd6f156")
    # print(result)
    # result = obj.update_one()
    # result = obj.update_more()
    # print(result.matched_count)
    # print(result.modified_count)
    # result = obj.delete_one()
    result = obj.delete_more()
    print(result.deleted_count)


if __name__ == '__main__':
    main()
