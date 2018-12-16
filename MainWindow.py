from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QHBoxLayout, QMenuBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from MainTableWidget import MainTableWidget
import os, shutil

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
        menu  = QMenuBar()

        exitButton = QAction(QIcon('images/exit.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close_app)
        menu.addAction(exitButton)

        mainMenu.setCornerWidget(menu)
        self.showFullScreen()
    
    # Function to delete equation images after closing the app
    def close_app(self):
        folder = 'equations'
        for the_file in os.listdir(folder):
            
            # Delete all files except about.txt
            if(str(the_file) != "about.txt"):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    #elif os.path.isdir(file_path): shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
                
        self.close()
