import sys
from PyQt5.Qt import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.setWindowTitle("fuck")
        self.steup_ui()
    def timerEvent(self, *args, **kwargs): # 增加事件函数
        x = self.width()
        y = self.height()
        self.resize(x+10,y+10)
    def steup_ui(self):
        lable = QLabel(self)
        lable.setText("你妹的")
        lable.move(250,250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())


