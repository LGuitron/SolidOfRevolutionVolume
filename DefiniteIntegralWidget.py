from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QPixmap
from GlobalVariables import GlobalVariables
from LatexFormulas import createLatexFormula
from sympy import integrate, var, latex, sympify
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
        
        if(len(GlobalVariables.mathFunctionsList)>0):
            self.mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
            self.calculateIntegrals()
        

    # Function for calculating definite integral of each part
    def calculateIntegrals(self):
        
        if(self.labelParts != None):
            for label in self.labelParts:
                label.setText("")
                self.topLayout.removeWidget(label)
        
        self.labelParts = []
        self.exactVolume = 0
        i = 1
        for part in self.mathFunction:
            
            
            part_label           = QLabel()
            part_solved_integral = QLabel() 
            part_volume_label    = QLabel() 
            
            # Integrate this part as function ^ 2 from x0 to x1
            radius_squared = part.f_expression ** 2
            
            # Check if the expression has an X in order to integrate, otherwise leave it like that
            if("x" in  str(radius_squared)):
                integral       = integrate(radius_squared)
            else:
                integral       = radius_squared * sympify("x")
                
            evalx0         = integral.subs(var('x'), part.x0)
            evalx1         = integral.subs(var('x'), part.x1)
            
            # Volume of current part obtained by definite integral and multiplying by PI
            partVolume = np.pi * (evalx1 - evalx0)
            
            
            # Generate Latex formula for current part and diplay it
            #createLatexFormula(r'$Volumen_{parte' +  str(i) +'} = \pi \int_{'+ str(part.x0) +'}^{'+str(part.x1)+'}'+ latex(radius_squared)+r'dx = \pi \left('+latex(integral)+ r'\right)\vert_{'+str(part.x0)+'}^{'+str(part.x1)+'} = '+latex(partVolume)+'$', 'equations/part'+ str(i)+'.png', 100)
            
            createLatexFormula(r'$Volumen_{parte' +  str(i) +'} = \pi \int_{'+ str(part.x0) +'}^{'+str(part.x1)+'}'+ latex(radius_squared)+r'dx$', 'equations/part'+ str(i)+'.png', 100)
            
            createLatexFormula(r'$Volumen_{parte' +  str(i) +'} = \pi \left('+latex(integral)+ r'\right)\vert_{'+str(part.x0)+'}^{'+str(part.x1)+'}$', 'equations/solved_integral_'+ str(i)+'.png', 100)
            
            createLatexFormula(r'$Volumen_{parte' +  str(i) +'} = '+latex(partVolume)+'$', 'equations/part_volume_'+ str(i)+'.png', 100)
            
            
            part_label.setPixmap(QPixmap('equations/part'+ str(i)+'.png'))
            part_label.setMaximumWidth(0.5 * GlobalVariables.screenWidth)
            
            part_solved_integral.setPixmap(QPixmap('equations/solved_integral_'+ str(i)+'.png'))
            part_solved_integral.setMaximumWidth(0.5 * GlobalVariables.screenWidth)
            
            part_volume_label.setPixmap(QPixmap('equations/part_volume_'+ str(i)+'.png'))
            part_volume_label.setMaximumWidth(0.5 * GlobalVariables.screenWidth)
            
            i += 1
            
            self.exactVolume += partVolume
            self.labelParts.append(part_label)
            self.labelParts.append(part_solved_integral)
            self.labelParts.append(part_volume_label)
            
            self.topLayout.addWidget(self.labelParts[len(self.labelParts)-3])
            self.topLayout.addWidget(self.labelParts[len(self.labelParts)-2])
            self.topLayout.addWidget(self.labelParts[len(self.labelParts)-1])
            
            # Add empty label between parts
            self.topLayout.addWidget(QLabel(""))
            
        # Generate Latex formula for results part and diplay it
        createLatexFormula(r'$Volumen_{exacto} = '+latex(self.exactVolume)+'$', 'equations/exactVolume.png', 100)
        self.labelVolume.setPixmap(QPixmap('equations/exactVolume.png'))
        self.labelVolume.setMaximumWidth(0.5 * GlobalVariables.screenWidth)
        
        try:
            createLatexFormula(r'$Volumen_{redondeado} = '+latex(float(self.exactVolume))+'$', 'equations/approxVolume.png', 100)
            self.roundedVolume.setPixmap(QPixmap('equations/approxVolume.png'))
            self.roundedVolume.setMaximumWidth(0.5 * GlobalVariables.screenWidth)
        except:
            self.roundedVolume = QLabel()
        
        self.setLayout(self.layout)
