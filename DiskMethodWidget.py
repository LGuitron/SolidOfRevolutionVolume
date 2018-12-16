from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIntValidator, QPixmap
from GlobalVariables import GlobalVariables
from DiskMethodPlot import DiskMethodPlot
from DiskMethodInteractivePlot import DiskMethodInteractivePlot
from SolidRevCalculations import calculateCoordinates, calculateVolume
from LatexFormulas import createLatexFormula

class DiskMethodWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.layoutFormulas = QHBoxLayout()
        
        # Display equation for volume aproximation by this method
        self.deltaxEquation = QLabel()
        self.radiusEquation = QLabel()
        self.volumeEquation = QLabel()
        
        # Get user input for number of disks
        self.label = QLabel()
        self.label.setText("Número de discos (Entre 1 y 999,999)=")
        
        self.input_section = QLineEdit()
        self.input_section.setValidator(QIntValidator(1, 999999))
        self.input_section.setText("5")
        self.input_section.textChanged.connect(self.updatePlot)

        self.m              = None
        self.layoutA        = None
        self.layoutPlot     = None          # Layout that includes button and plot widgets
        
        self.addedVolumeLabel = False
        self.interactiveGraph = None
        self.interactiveGraphButton = None
        
        self.function_circle_points = 15    # Points displayed in circle perimeter
        self.function_x_points      = 2     # X points to display per each cylinder
        
        # X, Y, and Z coordinates to be plotted
        self.X = None
        self.Y = None
        self.Z = None

        # Disks to be displayed and disks for volume approximation
        self.maxDisplayedDisks   = 200
        self.displayedDisks      = 0
        self.diskAmount          = 0

        self.volumeApproximation = 0 
        
        # Currently displayed math function
        self.mathFunction = None
        
    # Update plot whenever a new function is selected
    def updatePlot(self):

        if(len(GlobalVariables.mathFunctionsList)==0):
            return
            
        self.input_section.setReadOnly(True)
        
        # Add input section when the first function is added
        if(self.layoutA == None):
            self.layoutA = QVBoxLayout()
            self.layoutA.setDirection(QVBoxLayout.Direction.LeftToRight)
            self.layoutA.addWidget(self.label)
            self.layoutA.addWidget(self.input_section)
            self.layout.addLayout(self.layoutA)
            
        # Force a minimum of 1 disk
        if(self.input_section.text()=='' or int(self.input_section.text())==0):
            self.diskAmount = 1
        else:
            self.diskAmount = int(self.input_section.text())
        
        # Determine if the amount of disks plotted has changed in order to refresh the plot
        refreshPlot = False
        if(self.displayedDisks != min(self.diskAmount, self.maxDisplayedDisks)):
            self.displayedDisks = min(self.diskAmount, self.maxDisplayedDisks)
            refreshPlot = True
        
        # Get currently selected function
        if(self.mathFunction != GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]):
            self.mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
            refreshPlot = True

        x0           = self.mathFunction[0].x0
        x1           = self.mathFunction[len(self.mathFunction)-1].x1
        deltax       = (x1-x0)/self.displayedDisks

        # Calculate volume Approximation
        self.volumeApproximation = calculateVolume(self.mathFunction, self.diskAmount)
        
        if(refreshPlot):
            # Calculate X, Y, and Z coordinates for plots
            self.X, self.Y, self.Z   = calculateCoordinates(self.mathFunction, self.displayedDisks, self.function_circle_points, self.function_x_points)
            if(self.m != None):
                self.layoutPlot.removeWidget(self.m)
            self.m = DiskMethodPlot(self)
        
        # Calculate approximation for cylinder volume and write equations
        # Create equations png files
        createLatexFormula(r'$\Delta x = \frac{x_1-x_0}{n} = \frac{'+ str.format('{0:.4f}', x1) + '-' + str.format('{0:.4}', x0) +'}{'+ str(self.diskAmount) +'} = ' + str.format('{0:.4f}', deltax) + '$', 'equations/formula_deltax.png', 120)
        
        createLatexFormula(r'$r_i = f \left(x_0 + \Delta x(i - \frac{1}{2}) \right) = f \left('+ str.format('{0:.4f}',x0) + '+' + str.format('{0:.4f}',deltax) +'(i - ' +r'\frac{1}{2})\right)$', 'equations/formula_radius.png', 120)
        
        createLatexFormula(r'$V \approx \pi \Delta x \sum_i^n r_i^2$ = ' + str(self.volumeApproximation), 'equations/formula_volume.png', 120)
        
        # Set Equation QPixmaps
        self.deltaxEquation.setPixmap(QPixmap('equations/formula_deltax.png'))
        self.radiusEquation.setPixmap(QPixmap('equations/formula_radius.png'))
        self.volumeEquation.setPixmap(QPixmap('equations/formula_volume.png'))

        # Add Widgets for volume approximation only once
        if(not self.addedVolumeLabel):
            self.addedVolumeLabel = True
            self.layoutFormulas.addWidget(self.deltaxEquation)
            self.layoutFormulas.addWidget(self.radiusEquation)
            self.layout.addLayout(self.layoutFormulas)
            self.layout.addWidget(self.volumeEquation)
        
        
        # Layout that includes button and plot widgets
        if(self.layoutPlot == None):
            self.layoutPlot = QVBoxLayout()
            self.layoutPlot.setDirection(QVBoxLayout.Direction.BottomToTop)
            self.interactiveGraphButton = QPushButton("Abrir gráfica Interactiva")
            self.interactiveGraphButton.clicked.connect(self.openInteractivePlot)
            self.layoutPlot.addWidget(self.interactiveGraphButton)    
            self.layout.addLayout(self.layoutPlot)
        
        self.layoutPlot.addWidget(self.m)
        self.setLayout(self.layout)
        self.input_section.setReadOnly(False)
    
    def openInteractivePlot(self):
        if(self.interactiveGraph != None):
            self.layout.removeWidget(self.interactiveGraph)
        
        self.interactiveGraph = DiskMethodInteractivePlot(self)
        self.layout.addWidget(self.interactiveGraph)
