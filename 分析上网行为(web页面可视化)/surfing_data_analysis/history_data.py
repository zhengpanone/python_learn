# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/8/23 11:02
"""

# import lib
import sqlite3


def query_sqlite_db(history_db, query):
    """
    查询数据库内容
    :param history_db: 历史文件路径
    :param query:   sql语句
    :return:
    """
    # 查询sqlite数据库
    conn = sqlite3.connect(history_db)
    cursor = conn.cursor()

    select_statement = query

    cursor.execute(select_statement)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_history_data(history_file_path):
    """
    获取排序后的历史数据
    :param history_file_path:
    :return:
    """
    try:
        select_statement = "SELECT * from urls"
        result = query_sqlite_db(history_file_path, select_statement)

        result_sort = sorted(result, key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
        return result_sort
    except Exception as e:
        return e


def get_search_word(history_file_path):
    try:
        select_statement = "select * from "
        result = query_sqlite_db(history_file_path, select_statement)

        result_sort = sorted(result, key=lambda x: (x[0]))

        return result_sort
    except Exception as e:
        return e


if __name__ == '__main__':
    get_history_data("./History")
