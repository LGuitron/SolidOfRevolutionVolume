from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from GlobalVariables import GlobalVariables
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    GlobalVariables.screenWidth, GlobalVariables.screenHeight = screen_resolution.width(), screen_resolution.height()
    w = MainWindow()
    sys.exit(app.exec_())
