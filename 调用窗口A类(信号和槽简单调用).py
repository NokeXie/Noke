# -*- coding: utf-8 -*-
from 定义一个窗口A类 import *
from PyQt5.Qt import *
import sys
app = QApplication(sys.argv)
win = window()
btn = QPushButton(win)
btn.setText("点击我")
def cao1():
    print("点我干嘛")
btn.clicked.connect(cao1)

def cao(nwww): #槽函数
    print(nwww)
win.objectNameChanged.connect(cao)

win.setObjectName("sadasdasdasd111111111111111111111111111")
print(win.objectName())

#btn.clicked.connect(cao) #点击BTN按钮触发槽函数cao()
win.show()
sys.exit(app.exec_())