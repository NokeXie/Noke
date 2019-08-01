# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys
class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print(self.focusWidget())


# 1.创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1 创建控件
window = Window()
# 2.2 控件的设置
window.setWindowTitle("获取焦点")
window.resize(500,500)
btn = QPushButton(window)
lel = QLineEdit(window)
lel.move(50,50)
lel2 = QLineEdit(window)
lel2.move(100,100)
lel3 = QLineEdit(window)
lel3.move(150,150)
meue = QMenu()
meue.addAction("asdasdas")
meue.setTitle("sdasda")
btn.setMenu(meue)
# lel2.setFocus()
# lel2.setFocusPolicy(Qt.TabFocus)
# lel3.setFocusPolicy(Qt.ClickFocus)
# 获取窗口内部，所有的子控件那个获取焦点的控件

# 2.3 展示控件
window.show()
print(window.focusWidget())
# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
