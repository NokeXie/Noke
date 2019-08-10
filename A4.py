import sys
from PyQt5.Qt import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.setWindowTitle("fuck")
        self.steup_ui()
    def steup_ui(self):
        lable = QLabel(self)
        lable.setText("你妹的")
        lable.move(250,250)


class MyLable(QLabel):
    def enterEvent(self, *args, **kwargs):
        print("你进来干嘛")
        self.setText("来了，老弟")
    def leaveEvent(self, *args, **kwargs):
        self.setText("走了，老弟")
        print("拜拜")
    def keyPressEvent(self, evt):
        QKeyEvent
        if evt.modifiers()== Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_S:
            lable.setText("asdasdasdasdasd")
            print("asdasdasdas")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    lable = MyLable(win)
    lable.resize(300,300)
    lable.setText("asdasdasdasdasd")
    lable.move(100,100)
    lable.setStyleSheet("background-color:yellow;")
    lable.grabKeyboard()
    win.show()
    sys.exit(app.exec_())