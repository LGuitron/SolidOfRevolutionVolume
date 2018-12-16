from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from GlobalVariables import GlobalVariables
from sympy import integrate, var
import numpy as np

class DefiniteIntegralWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout           = QVBoxLayout()
        self.labelParts       = None
        self.mathFunction     = None
        self.exactVolume      = 0
        self.labelVolume      = QLabel()
        self.roundedVolume    = QLabel()
        self.topLayout        = QVBoxLayout()   # Layout used for displaying volume calculation for each part
        self.bottomLayout     = QVBoxLayout()   # Layout used for displaying final result
        self.bottomLayout.addWidget(self.labelVolume)
        self.bottomLayout.addWidget(self.roundedVolume)
        
        self.layout.addLayout(self.topLayout)
        self.layout.addLayout(self.bottomLayout)
        
        #self.addedVolumeLabel = False
        
    # Update integral whenever a new function is selected
    def updatePlot(self):
        self.mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
        self.calculateIntegrals()
        

    # Function for calculating definite integral of each part
    def calculateIntegrals(self):
        
        if(self.labelParts != None):
            for label in self.labelParts:
                label.setText("")
                self.topLayout.removeWidget(label)
                #self.layout.removeWidget(label)
        
        self.labelParts = []
        self.exactVolume = 0
        i = 1
        for part in self.mathFunction:
            
            
            part_label = QLabel()
            
            
            # Integrate this part as function ^ 2 from x0 to x1
            radius_squared = part.f_expression ** 2
            integral       = integrate(radius_squared)
            evalx0         = integral.subs(var('x'), part.x0)
            evalx1         = integral.subs(var('x'), part.x1)
            
            # Volume of current part obtained by definite integral and multiplying by PI
            partVolume = np.pi * (evalx1 - evalx0)
            
            part_label.setText("Volumen Parte " + str(i) + " =     PI * Integral (" +  str(radius_squared) + ")  from " + str(part.x0) + " to " + 
                               str(part.x1)  + " =         " +  "PI * (" + str(evalx1) + " - " + str(evalx0) + ")  =  " + str(partVolume))
            i += 1
            
            self.exactVolume += partVolume
            self.labelParts.append(part_label)
            self.topLayout.addWidget(self.labelParts[len(self.labelParts)-1])

        self.labelVolume.setText("Volumen (Expresión exacta) = " + str(self.exactVolume))
        self.roundedVolume.setText("Volumen (Redondeado) = " + str(float(self.exactVolume)))
        self.setLayout(self.layout)
