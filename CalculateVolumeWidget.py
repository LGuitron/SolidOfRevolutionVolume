from PyQt5.QtWidgets import QWidget, QVBoxLayout,QLabel, QLineEdit
from PyQt5.QtGui import QIntValidator
from GlobalVariables import GlobalVariables
from DiskMethodPlot import DiskMethodPlot

class CalculateVolumeWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Get user input for number of disks
        self.label = QLabel()
        self.label.setText("Número de discos =")
        
        self.input_section = QLineEdit()
        self.input_section.setValidator(QIntValidator(1,999))
        self.input_section.setText("5")
        self.input_section.textChanged.connect(self.updatePlot)
        
        self.m           = None
        self.layoutA     = None
        self.labelVolume = QLabel()
        
        self.addedVolumeLabel = False
        
    # Update plot whenever a new function is selected
    def updatePlot(self):
        
        # Add input section when the first function is added
        if(self.layoutA == None and len(GlobalVariables.mathFunctionsList)==1):
            self.layoutA = QVBoxLayout()
            self.layoutA.setDirection(QVBoxLayout.Direction.LeftToRight)
            self.layoutA.addWidget(self.label)
            self.layoutA.addWidget(self.input_section)
            self.layout.addLayout(self.layoutA)
        
        if(self.m != None):
            self.layout.removeWidget(self.m)
        self.m = DiskMethodPlot(self)
        
        self.labelVolume.setText("Volumen de cilindros = " + str(self.m.solidVolume))
        if(not self.addedVolumeLabel):
            self.addedVolumeLabel = True
            self.layout.addWidget(self.labelVolume)
            
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)        
