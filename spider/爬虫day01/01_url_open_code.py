# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/6/5 11:35
"""

# import lib
import string
import urllib.request
import urllib.parse


def load_data():
    url = "http://www.baidu.com/"
    # http响应对象
    response = urllib.request.urlopen(url)
    data = response.read()
    print(data.decode("utf-8"))
    pass


def get_method_params():
    url = "http://www.baidu.com/s?wd="
    name = "美女"
    final_url = url + name
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(encode_new_url)
    print(response.read().decode("utf-8"))


get_method_params()
