import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('QTableView表格视图的例子')
        self.resize(500,300)

        #设置数据层次结构，4行4列
        self.model=QStandardItemModel(4,4)
        #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['标题1','标题2','标题3','标题4'])
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1 创建控件
window = QWidget()
T1 = Table(window)
T1.move(20,20)
T1.setStyleSheet("backgroup-color:yellow")
window.show()
sys.exit(app.exec_())