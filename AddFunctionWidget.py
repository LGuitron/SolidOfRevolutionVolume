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

        self.layout = QVBoxLayout(self)
        self.mainTableWidget = parent
        
        # Text Display
        self.labelInfo= QLabel()
        self.labelInfo.setText("Introduce una función: ")

        # Input section
        self.layoutInput = QVBoxLayout()
        self.layoutInput.setDirection(QVBoxLayout.Direction.LeftToRight)
        
        self.labelForm= QLabel()
        self.labelForm.setText("f(x) = ")
        
        self.input_section = QLineEdit()
        
        self.layoutInput.addWidget(self.labelInfo)
        self.layoutInput.addWidget(self.labelForm)
        self.layoutInput.addWidget(self.input_section)
        self.layout.addLayout(self.layoutInput)
        
        
        # Form submission
        self.acceptButton = QPushButton("Aceptar")
        self.layout.addWidget(self.acceptButton)
        self.acceptButton.clicked.connect(self.pushFunction)

        self.setLayout(self.layout)

    # Function for adding polinomial function to the list of functions
    @pyqtSlot()
    def pushFunction(self):
        f_expression = sympify(self.input_section.text())
        GlobalVariables.mathFunctionsList.append(MathFunction(f_expression))
        self.mainTableWidget.updateListWidget(True)
