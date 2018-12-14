from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from GlobalVariables import GlobalVariables
from SolidRevPlot import SolidRevPlot
from SolidRevInteractivePlot import SolidRevInteractivePlot
from SolidRevCalculations import calculateCoordinatesSolidRev

class SolidRevWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.m = None
        self.interactiveGraph = None
        self.interactiveGraphButton = None
        
        self.function_circle_points = 30        # Points displayed in circle perimeter
        self.function_x_points      = 1000       # Points to be displayed along x axis
        
        # X, Y, and Z coordinates to be plotted
        self.X = None
        self.Y = None
        self.Z = None
        
    # Update plot whenever a new function is selected
    def updatePlot(self):

        if(self.m != None):
            self.layout.removeWidget(self.m)
        
        
        # Get currently selected function
        mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
        self.X, self.Y, self.Z   = calculateCoordinatesSolidRev(mathFunction, self.function_circle_points, self.function_x_points)
        
        self.m = SolidRevPlot(self)
        self.layout.addWidget(self.m)
        
        # Button for opening interactive plot
        if(self.interactiveGraphButton != None):
            self.layout.removeWidget(self.interactiveGraphButton)

        self.interactiveGraphButton = QPushButton("Abrir gráfica Interactiva")
        self.interactiveGraphButton.clicked.connect(self.openInteractivePlot)
        self.layout.addWidget(self.interactiveGraphButton)
            
        self.setLayout(self.layout)        
        
    def openInteractivePlot(self):
        if(self.interactiveGraph != None):
            self.layout.removeWidget(self.interactiveGraph)
        
        self.interactiveGraph = SolidRevInteractivePlot(self)
        self.layout.addWidget(self.interactiveGraph)
