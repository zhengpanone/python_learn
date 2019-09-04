# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/8/23 15:46
"""

# import lib
import dash

# dash是一款基于python的web轻量级框架，无需js即可轻松运行
# 适合用于比较简单的web页面的快速部署，如数据可视化，图表展示等
# 复杂页面不建议使用dash进行开发
# dash官网: https://dash.plot.ly/

# 配置一个dash服务器
app = dash.Dash(__name__)
