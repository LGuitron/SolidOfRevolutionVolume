from sympy import var
from sympy import sympify

from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import pyqtSlot, QObject

from MathFunction import MathFunction
from GlobalVariables import GlobalVariables

# UI to be displayed for adding polinomial function
class AddFunctionWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.currentFunction = []                # Store current function as an array of MathFuncion objects
        self.currentFunctionText = QLabel()      # Store text for current function

        self.layout = QVBoxLayout(self)
        self.mainTableWidget = parent
        
        # Function Input section
        self.layoutInput = QVBoxLayout()
        self.layoutInput.setDirection(QVBoxLayout.Direction.LeftToRight)

        
        # Interval input
        self.input_section = QLineEdit()
        self.x0 = QLineEdit()
        self.x0.setValidator(QDoubleValidator())
        self.x0.setMaximumWidth(0.1*GlobalVariables.screenWidth)
                
        self.x1 = QLineEdit()
        self.x1.setValidator(QDoubleValidator())
        self.x1.setMaximumWidth(0.1*GlobalVariables.screenWidth)

        #self.layoutInput.addWidget(self.labelInfo)
        self.layoutInput.addWidget(QLabel("f(x) = "))
        self.layoutInput.addWidget(self.input_section)
        self.layoutInput.addWidget(QLabel("Intervalo: ("))
        self.layoutInput.addWidget(self.x0)
        self.layoutInput.addWidget(QLabel(", "))
        self.layoutInput.addWidget(self.x1)
        self.layoutInput.addWidget(QLabel(")"))

        # Add new part button
        self.addPartButton = QPushButton("Agrega nueva parte")
        self.addPartButton.clicked.connect(self.addPart)
        
        # Function submission
        self.acceptButton = QPushButton("Aceptar")
        self.acceptButton.clicked.connect(self.pushFunction)
        
        
        # Show examples
        
        self.layout.addWidget(QLabel("Introduce una función: \n\nEjemplos: \n\nsin(2*x) \n4*x^3+2*x^2+4*x+1 \nexp(2*x) \nln(x) \narctan(2*x \nx^(1/2))"))
        self.layout.addLayout(self.layoutInput)
        self.layout.addWidget(self.currentFunctionText)
        self.layout.addWidget(self.addPartButton)
        self.layout.addWidget(self.acceptButton)

        self.setLayout(self.layout)
    
    # Function for adding new part to the function
    @pyqtSlot()
    def addPart(self):
        
        # Process inputs from last part
        f_expression = sympify(self.input_section.text())
        
        
        if(self.x0.text()=='' or self.x0.text()=='-'):
            x0 = 0
        else:
            x0 = float(self.x0.text())
        
        if(self.x1.text()=='' or self.x1.text()=='-'):
            x1 = 0
        else:
            x1 = float(self.x1.text())

        # Append last part to the currentFunction List
        newMathFunction = MathFunction(f_expression, x0, x1)
        self.currentFunction.append(newMathFunction)
        
        if(len(self.currentFunction)==1):
            self.currentFunctionText.setText("Función actual: \n\n")
        
        self.currentFunctionText.setText(self.currentFunctionText.text() + str(newMathFunction) + "\n")

        # Lock x0 for next function
        self.x0.setText(str(newMathFunction.x1))
        self.x0.setReadOnly(True)
        

    # Function for adding function to the list of functions
    @pyqtSlot()
    def pushFunction(self):
        # Add Last part to the current function
        if(len(self.currentFunction)>0):
            GlobalVariables.mathFunctionsList.append(self.currentFunction)
            self.currentFunction = []
            self.currentFunctionText.setText("")
            self.x0.setReadOnly(False)
            self.mainTableWidget.updateListWidget(True)
