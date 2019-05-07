from PyQt5.Qt import *
import sys
def text():
    k = [1,2,3,4,5]
    return k[4]
app = QApplication(sys.argv)
win = QWidget()
win.resize(500,500)
win.move(700,200)
lable = QLabel(win)
lable.resize(200,200)
lable.move(50,50)
lable.setText(str(text()))
def cao():
    lable.setText("sdasdas%d"%text() + "\n"
                  "asdasdasdasd%d"%text())
    lable.setStyleSheet("background-color:green;")
    print(lable.text())
btn = QPushButton(win)
btn.resize(100,100)
btn.move(200,100)
btn.setText("确定")
btn.clicked.connect(cao)
win.show()
sys.exit(app.exec_())