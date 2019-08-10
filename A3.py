from PyQt5.Qt import *
import sys
class Window(QWidget):
    def mouseMoveEvent(self,mv):
        print("asdasdasdasd",mv.localPos())
        label1 = self.findChild(QLabel)
        label1.move(mv.localPos().x(),mv.localPos().y())
    def moveEvent(self,qe):
        print("asdasdasdasdasd11111")

app = QApplication(sys.argv)
window = Window()
window.resize(500,500)
#window.setMouseTracking(True)
pixmap = QPixmap(r"C:\Users\Root\Desktop\1.png").scaled(50,50)
cursor = QCursor(pixmap)
window.setCursor(cursor)
# label = QLabel(window)
# label.setText("我最帅asdasdasda")
# label.move(100,100)
# label.setStyleSheet("background-color:red;")
# label.adjustSize()
label1= QLabel(window)
label1.setText("我最帅asdasdasda")
label1.move(130,130)
label1.setStyleSheet("background-color:red;")
label1.adjustSize()
window.show()
sys.exit(app.exec_())