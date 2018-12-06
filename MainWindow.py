from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from MainTableWidget import MainTableWidget

# Main window with navigation
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.setWindowTitle("Volumen de Sólidos de Revolución con Métodos Numéricos")
        self.table_widget = MainTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.initUI()

    # Function for main window base UI (Shared between all windows in this file)
    def initUI(self):
        
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        exitButton = QAction(QIcon('images/exit.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.showFullScreen()
