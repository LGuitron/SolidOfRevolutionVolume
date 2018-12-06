from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import pyqtSlot, QObject

from FormUtilities import addParameters
from MathFunction import MathFunction
from GlobalVariables import GlobalVariables

# UI to be displayed for adding polinomial function
class AddPolinomialWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.mainTableWidget = parent.parent
        
        # parameter information
        self.labelInfo= QLabel()
        self.labelInfo.setText("Agrega los parámetros de la función polinomial con la siguiente forma:")
        self.layout.addWidget(self.labelInfo)
        
        self.labelForm= QLabel()
        self.labelForm.setText("f(x) = Ax^3 + Bx^2 + Cx + D")
        self.layout.addWidget(self.labelForm)

        # parameters and input sections
        self.parameters     = ["A","B","C","D"]
        self.input_sections = []
        
        # Input Form (allows floats only)
        self.validator = QDoubleValidator()
        addParameters(self.layout, self.validator, "0", self.parameters, self.input_sections)
        
        # Form submission
        self.acceptButton = QPushButton("Aceptar")
        self.layout.addWidget(self.acceptButton)
        self.acceptButton.clicked.connect(self.pushPolinomialFunction)

        self.setLayout(self.layout)

    # Function for adding polinomial function to the list of functions
    @pyqtSlot()
    def pushPolinomialFunction(self):

        f_type = "polinomial"
        f_params_dict = {}
        
        for i in range (len(self.input_sections)):
            if (self.input_sections[i].text()=="" or self.input_sections[i].text()=="-"):
                self.input_sections[i].setText("0")
            f_params_dict[self.parameters[i]] = self.input_sections[i].text()

        GlobalVariables.mathFunctionsList.append(MathFunction(f_type, f_params_dict))
        self.mainTableWidget.updateListWidget(True)
