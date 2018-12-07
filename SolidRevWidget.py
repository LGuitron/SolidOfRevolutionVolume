from PyQt5.QtWidgets import QWidget, QVBoxLayout
from GlobalVariables import GlobalVariables
from SolidRevPlot import SolidRevPlot

class SolidRevWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.m = None
        
    # Update plot whenever a new function is selected
    def updatePlot(self):
        
        if(self.m != None):
            self.layout.removeWidget(self.m)
        
        self.m = SolidRevPlot(self)
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)        
