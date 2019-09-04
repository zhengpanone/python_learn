# -*- coding:utf-8 -*-
# /usr/bin/env python
from PyQt5.Qt import *
import sys

# 实例化应用程序对象
app = QApplication(sys.argv)

print(app.arguments())
print(qApp.arguments())

window = QWidget()
window.setWindowTitle("PyQt5测试")
window.resize(500, 500)
window.move(400, 200)

label = QLabel(window)
label.setText("Hello GUI")
label.move(200, 200)

window.show()

# 让整个程序开始执行，并且进入到消息循环
sys.exit(app.exec_())
