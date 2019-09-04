# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/5/27 16:18
"""

# import lib
import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Window(QWidget):
    def __init__(self, title=""):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self, text=""):
        label = QLabel(self)
        label.setText(text)

    def QOBject_fater_class(self):
        mros = QObject.mro()
        for mro in mros:
            print(mro)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Window(title="PyQt5")
    window.QOBject_fater_class()
    window.setup_ui(text="test")
    window.show()

    sys.exit(app.exec_())
