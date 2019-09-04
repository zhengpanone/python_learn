# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/8/23 15:59
"""

# import lib
from app_configuration import app
import dash
from app_plot import *


def app_callback_function():
    @app.callback(
        dash.dependencies.Output('graph_website_count_rank', 'figure'),
        [
            dash.dependencies.Input('input_website_count_rank', 'value'),
            # dash.dependencies.Input('store_memory_history_data', 'value')
        ]
    )
    def update(value, store_memory_history_data):
        if store_memory_history_data:
            history_data = store_memory_history_data['history_data']
            figure = plot_bar_website_count_rank(value, history_data)
            return figure
        else:
            raise dash.exceptions.PreventUpdate("cancel the callback")

    return None
