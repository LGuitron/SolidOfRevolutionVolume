from PyQt5.QtWidgets import QWidget, QVBoxLayout
from Plot2D import Plot2D

class FunctionPlotWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.m = None
        
    # Update plot whenever a new function is selected
    def updatePlot(self):
        
        if(self.m != None):
            self.layout.removeWidget(self.m)
        
        self.m = Plot2D(self)
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)
