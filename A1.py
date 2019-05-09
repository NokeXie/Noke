from PyQt5.Qt import *
import sys
from 获取丹阳天气 import tianqi
app = QApplication(sys.argv)
win = QWidget()
win.resize(500,500)
win.move(700,200)
lable = QLabel(win)
lable.move(50,50)
lable.setText("获取天气")
lable.setStyleSheet("background-color:green;font:20px")
lable.adjustSize()
def cao():
    lable.setText(tianqi()) #tianqi()函数获取天气
    lable.adjustSize()
    lable.setStyleSheet("background-color:green;font:15px")
    print(lable.text())
btn = QPushButton(win)
btn.resize(100,100)
btn.move(300,100)
btn.setText("确定")
btn.clicked.connect(cao)
win.show()
sys.exit(app.exec_())