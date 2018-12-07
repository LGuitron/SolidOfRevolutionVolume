from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
#from PyQt5.QtGui import QIntValidator
#from GlobalVariables import GlobalVariables
from DiskMethodWidget import DiskMethodWidget

class CalculateVolumeWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        
        self.layout = QVBoxLayout(self)
        self.parent = parent
        
        # Array of indices of tabs with plots (for making updates when switching to them)
        self.tabsWithPlots = [0]
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = DiskMethodWidget(self)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Método de discos")
        #self.tabs.addTab(self.tab2,"Trigonométrica")
 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    
    # Update plot subtab
    def updatePlot(self):
        if(self.tabs.currentIndex() in self.tabsWithPlots):
            self.tabs.currentWidget().updatePlot()
