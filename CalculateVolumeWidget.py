from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from DiskMethodWidget import DiskMethodWidget
from DefiniteIntegralWidget import DefiniteIntegralWidget

class CalculateVolumeWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        
        self.layout = QVBoxLayout(self)
        self.parent = parent
        
        # Array of indices of tabs with plots (for making updates when switching to them)
        self.tabsWithPlots = [0,1]
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = DiskMethodWidget(self)
        self.tab2 = DefiniteIntegralWidget(self)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Método de discos")
        self.tabs.addTab(self.tab2,"Integral definida")
        
        # Function whenever a new tab is clicked
        self.tabs.currentChanged.connect(self.updatePlot)
        
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    
    # Update plot subtab
    def updatePlot(self):
        if(self.tabs.currentIndex() in self.tabsWithPlots):
            self.tabs.currentWidget().updatePlot()
