# -*- coding: utf-8 -*-

import MySQLdb

try:
    # 创建连接
    conn = MySQLdb.connect(host="127.0.0.1",
                           user='root', passwd="root", port=3306, db='fisher')
    # 创建游标
    cursor = conn.cursor()
    # 执行查询
    cursor.execute("SELECT * FROM USER ")
    rest = cursor.fetchone()  # 返回元组
    print(rest)
    # 关闭连接
    conn.close()
except MySQLdb.Error as e:
    print("连接错误%s" % e)
