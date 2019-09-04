from app_configuration import app
from app_layout import app_layout
from app_callback import app_callback_function

# 设置网页标题
app.title = "Browser History Analysis"

# 设置网页标题
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# html元素布局
app.layout = app_layout

# 回调，用于更新web页面数据
# dash框架是前后端不分离的，所以仅仅适用于简单页面部署，复杂页面不推荐使用dash
app_callback_function()

if __name__ == '__main__':
    # 是否在本地运行
    app_local = True
    if app_local:
        app.run_server(host='127.0.0.1', debug=True, port=8090)
    else:
        app.run_server(host='0.0.0.0', debug=False, port='8090')
