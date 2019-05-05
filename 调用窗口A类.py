# -*- coding: utf-8 -*-
from 定义一个窗口A类 import *
from PyQt5.Qt import *
import sys
app = QApplication(sys.argv)
win = window()
win.startTimer(1000)  #增加定时器
win.show()
sys.exit(app.exec_())