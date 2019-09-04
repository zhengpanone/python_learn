# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/8/23 16:35
"""

# import lib
import plotly.graph_objs as go


def url_simplification(url):
    tmp_url = url

    try:
        url = url.split("//")
        url = url[1].split("/", 1)
        url = url[0].replace("wwww.", "")
        return url
    except IndexError:
        return tmp_url


def convert_to_number(value):
    try:
        x = int(value)
    except TypeError:
        return 0
    except ValueError:
        return 0
    except Exception as e:
        return 0
    return x


# 获取字典的前k个最大的子集合，按value
def get_top_k_from_dict(origin_dict, k):
    origin_dict_len = len(origin_dict)
    n = k
    if n > origin_dict_len:
        n = origin_dict_len
    new_data = sorted(origin_dict.items(), key=lambda item: item[1], reverse=True)
    new_data = new_data[:n]
    new_dict = {}
    for l in new_data:
        new_dict[l[0]] = l[1]
    return new_dict


def plot_bar_website_count_rank(value, history_data):
    # 频率词典
    dict_data = {}

    for data in history_data:
        url = data[1]
        # 简化url
        key = url_simplification(url)
        if key in dict_data.keys():
            dict_data[key] += 1
        else:
            dict_data[key] = 0
    # 筛选前k个频率最高
    k = convert_to_number(value)
    top_ten_dict = get_top_k_from_dict(dict_data, 10)

    figure = go.Figure(
        data=[
            go.Bar(
                x=[i for i in top_ten_dict.keys()],
                y=[i for i in top_ten_dict.values()],
                name='bar',
                marker=go.bar.Marker(
                    color='rgb(55,83,109)'
                )
            )
        ],
        layout=go.Layout(
            showlegend=False,
            margin=go.layout.Margin(l=40, r=0, t=40, b=30),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title='网站'),
            yaxis=dict(title='次数')
        )
    )
    return figure
