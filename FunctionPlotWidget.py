from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QDoubleValidator
from Plot2D import Plot2D
from GlobalVariables import GlobalVariables

class FunctionPlotWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Get user input for function domain
        self.label = QLabel()
        self.label.setText("Dominio de función = (")
        
        self.x0 = QLineEdit()
        self.x0.setValidator(QDoubleValidator())
        self.x0.setText(str(GlobalVariables.x0))
        self.x0.textChanged.connect(self.updatePlot)
                
        self.x1 = QLineEdit()
        self.x1.setValidator(QDoubleValidator())
        self.x1.setText(str(GlobalVariables.x1))
        self.x1.textChanged.connect(self.updatePlot)

        self.m       = None
        self.layoutA = None
        
    # Update plot whenever a new function is selected
    def updatePlot(self):
        
        if(self.x0.text()=='' or self.x0.text()=='-'):
            GlobalVariables.x0 = 0
        else:
            GlobalVariables.x0 = float(self.x0.text())
        
        if(self.x1.text()=='' or self.x1.text()=='-'):
            GlobalVariables.x1 = 0
        else:
            GlobalVariables.x1 = float(self.x1.text())
        
        # Set upper limit to at least the value of the lower limit
        if(GlobalVariables.x1 < GlobalVariables.x0):
            GlobalVariables.x1 = GlobalVariables.x0
        
        # Add input section when the first function is added
        if(self.layoutA == None):
            labelComma = QLabel()
            labelComma.setText(", ")
            
            labelParenthesis = QLabel()
            labelParenthesis.setText(")")
            
            self.layoutA = QVBoxLayout()
            self.layoutA.setDirection(QVBoxLayout.Direction.LeftToRight)
            

            self.layoutA.addWidget(self.label)
            self.layoutA.addWidget(self.x0)
            self.layoutA.addWidget(labelComma)
            self.layoutA.addWidget(self.x1)
            self.layoutA.addWidget(labelParenthesis)
            
            self.layout.addLayout(self.layoutA)
        
        
        if(self.m != None):
            self.layout.removeWidget(self.m)
        
        self.m = Plot2D(self)
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)
