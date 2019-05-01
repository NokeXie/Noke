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
        lable.setText("你没1212121212121")
        lable.move(250,250)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())