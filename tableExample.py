from PyQt5.QtWidgets import QWidget, QTabWidget,QVBoxLayout, QListWidget, QCheckBox, QButtonGroup, QLabel, QListWidgetItem, QListView, QTableWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter
import sys

#imagePath = "equations/exactVolume.png"

class ImgWidget1(QLabel):

    def __init__(self, parent=None, imagePath=None):
        super(ImgWidget1, self).__init__(parent)
        pic = QPixmap(imagePath)
        self.setPixmap(pic)
'''
class ImgWidget2(QWidget):

    def __init__(self, parent=None):
        super(ImgWidget2, self).__init__(parent)
        self.pic = QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pic)
'''

class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        tableWidget = QTableWidget(10, 2, self)
        tableWidget.setCellWidget(0, 1, ImgWidget1(self, "equations/exactVolume.png"))
        tableWidget.setCellWidget(1, 1, ImgWidget1(self, "equations/exactVolume.png"))

if __name__ == "__main__":
    app = QApplication([])
    wnd = Widget()
    wnd.show()
    sys.exit(app.exec_())
