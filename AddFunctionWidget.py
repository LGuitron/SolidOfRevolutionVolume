from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from AddPolinomialWidget import AddPolinomialWidget
from MathFunction import MathFunction

class AddFunctionWidget(QWidget):

    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        
        self.layout = QVBoxLayout(self)
        self.parent = parent
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = AddPolinomialWidget(self)
        self.tab2 = QWidget()
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Polinomial")
        self.tabs.addTab(self.tab2,"Trigonométrica")
 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
