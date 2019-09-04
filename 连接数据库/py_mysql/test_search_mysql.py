# -*- coding: utf-8 -*-
import MySQLdb


class MysqlSearch:
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            # 创建连接
            self.conn = MySQLdb.connect(host="127.0.0.1",
                                        user='root', passwd="root", port=3306, db='fisher')
        except MySQLdb.Error as e:
            print("连接错误%s" % e)

    def close_conn(self):
        try:
            if self.conn:
                print(self.conn)
                self.conn.close()
                print("关闭连接成功")
        except MySQLdb.Error as e:
            print('Error:%s' % e)

    def get_one(self):
        """查询一条数据"""
        # SQL
        sql = "SELECT * FROM USER WHERE `ID`=%s;"
        # cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ("1",))
        # print("共有%d 行" % cursor.rowcount)
        # print(cursor.description)
        # result
        # result = cursor.fetchone()
        result = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理result
        # print(result['nickname'])
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return result

    def get_more(self):
        """查询多条数据"""
        # SQL
        sql = "SELECT * FROM USER WHERE `STATUS`=%s;"
        # cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ("1",))
        result = [dict(zip([k[0] for k in cursor.description], row))
                  for row in cursor.fetchall()]
        # 处理result
        # print(result['nickname'])
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return result

    def get_page(self, page, page_size):
        """分页查询"""
        offset = (page - 1) * page_size
        # SQL
        sql = "SELECT * FROM USER WHERE `STATUS`=%s DESC LIMIT %s,%s;"
        # cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ("1", offset, page_size))
        result = [dict(zip([k[0] for k in cursor.description], row))
                  for row in cursor.fetchall()]
        # 处理result
        # print(result['nickname'])
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return result

    def add_one(self):
        try:
            # SQL
            sql = "INSERT INTO `USER` (`NICKNAME`,`EMAIL`,`PASSWORD`) VALUE(%s,%s,%s)"
            # 获取连接和cursor
            cursor = self.conn.cursor()
            # 执行sql 提交到数据库
            cursor.execute(sql, ('test', 'test.qq.com', 'test', 'aaa'))
            # 提交事务
            self.conn.commit()
            # 关闭cursor 和连接
            cursor.close()

        except MySQLdb.Error as e:
            print('error :%s' % e)
            # self.conn.commit() # 部分提交
            # 异常回滚
            self.conn.rollback()
        self.close_conn()


def main():
    obj = MysqlSearch()
    # result = obj.get_one()
    # print(result)
    '''
    result = obj.get_more()
    for r in result:
        print(r)
        print("--------------------")
        '''
    obj.add_one()


if __name__ == '__main__':
    main()
