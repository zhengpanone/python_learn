# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/8/23 15:47
"""

# import lib

import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash_table.Format import Format, Scheme, Sign, Symbol

app_layout = html.Div([
    html.Div(
        className='row',
        children=[
            dcc.Input(
                id='upload_file_success_flag',
                type='number',
                value=1,
                style={
                    'display': 'none'
                }
            ),
            # 在浏览器中存储数据，每次刷新页面或者载入页面都会被清空
            dcc.Store(id="store_memory_history_data")

        ]
    ),
    html.Div(
        style={'margin-bottom': '150px'},
        children=[
            html.Div(
                style={'border-top-style': 'solid', 'border-bottom-style': 'solid'},
                className='row',
                children=[
                    html.Span(
                        children='页面访问次数排名, ',
                        style={'font-weight': 'bold', 'color': 'red'}
                    ),

                    html.Span(
                        children='显示个数:',
                    ),
                    dcc.Input(
                        id='input_website_count_rank',
                        type='text',
                        value=10,
                        style={'margin-top': '10px', 'margin-bottom': '10px'}

                    ),
                ]
            ), ]
    ),

    html.Div(
        style={'position': 'relative', 'margin': '0 auto', 'width': '100%', 'padding-bottom': '50%', },
        children=[
            dcc.Loading(
                children=[
                    dcc.Graph(
                        id='graph_website_count_rank',
                        style={
                            'position': 'absolute', 'width': '100%', 'height': '100%', 'top': '0',
                            'left': '0', 'bottom': '0', 'right': '0'},
                        config={'displayModeBar': False},
                    ),
                ],
                type='dot',
                style={'position': 'absolute', 'top': '50%', 'left': '50%', 'transform': 'translate(-50%,-50%)'}
            ),
        ],
    ),

])
