from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QDoubleValidator
from Plot2D import Plot2D
from GlobalVariables import GlobalVariables

class FunctionPlotWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.m       = None
        self.layoutA = None
        
    # Update plot whenever a new function is selected
    def updatePlot(self):
        
        if(self.m != None):
            self.layout.removeWidget(self.m)
        
        self.m = Plot2D(self)
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)
