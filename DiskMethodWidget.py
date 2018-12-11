from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,QLabel, QLineEdit
from PyQt5.QtGui import QIntValidator, QPixmap
from GlobalVariables import GlobalVariables
from DiskMethodPlot import DiskMethodPlot
from matplotlib import pylab, pyplot

class DiskMethodWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layoutFormulas = QHBoxLayout(self)
        
        # Display equation for volume aproximation by this method
        self.deltaxEquation = QLabel()
        self.radiusEquation = QLabel()
        self.volumeEquation = QLabel()
        
        # Get user input for number of disks
        self.label = QLabel()
        self.label.setText("Número de discos =")
        
        self.input_section = QLineEdit()
        self.input_section.setValidator(QIntValidator(1,999))
        self.input_section.setText("5")
        self.input_section.textChanged.connect(self.updatePlot)

        self.m              = None
        self.layoutA        = None
        self.labelVolume    = QLabel()

        self.addedVolumeLabel = False
        
    # Update plot whenever a new function is selected
    def updatePlot(self):
        
        # Add input section when the first function is added
        if(self.layoutA == None):
            self.layoutA = QVBoxLayout()
            self.layoutA.setDirection(QVBoxLayout.Direction.LeftToRight)
            self.layoutA.addWidget(self.label)
            self.layoutA.addWidget(self.input_section)
            self.layout.addLayout(self.layoutA)
        
        if(self.m != None):
            self.layout.removeWidget(self.m)
            
        self.m = DiskMethodPlot(self)
        
        # Calculate approximation for cylinder volume and write equations
        mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
        x0           = mathFunction[0].x0
        x1           = mathFunction[len(mathFunction)-1].x1
        deltax       = (x1-x0)/self.m.diskAmount
        
        # Create equations png files
        self.createLatexFormula(r'$\Delta x = \frac{x_1-x_0}{n} = \frac{'+ str.format('{0:.3f}', x1) + '-' + str.format('{0:.3f}', x0) +'}{'+ str(self.m.diskAmount) +'} = ' + str.format('{0:.3f}', deltax) + '$', 'equations/formula_deltax.png', 120)
        
        self.createLatexFormula(r'$r_i = f \left(x_0 + \Delta x(i - \frac{1}{2}) \right) = f \left('+ str.format('{0:.3f}',x0) + '+' + str.format('{0:.3f}',deltax) +'(i - ' +r'\frac{1}{2})\right)$', 'equations/formula_radius.png', 120)
        
        self.createLatexFormula(r'$V \approx \pi \Delta x \sum_i^n r_i^2$ = ' + str(self.m.solidVolume), 'equations/formula_volume.png', 120)
        
        # Set Equation QPixmaps
        self.deltaxEquation.setPixmap(QPixmap('equations/formula_deltax.png'))
        self.radiusEquation.setPixmap(QPixmap('equations/formula_radius.png'))
        self.volumeEquation.setPixmap(QPixmap('equations/formula_volume.png'))
        
        
        #self.labelVolume.setText("Volumen de cilindros = " + str(self.m.solidVolume))

        # Add Widgets for volume approximation only once
        if(not self.addedVolumeLabel):
            self.addedVolumeLabel = True
            self.layoutFormulas.addWidget(self.deltaxEquation)
            self.layoutFormulas.addWidget(self.radiusEquation)
            self.layout.addLayout(self.layoutFormulas)
            self.layout.addWidget(self.volumeEquation)
            #self.layout.addWidget(self.labelVolume)
            
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)        

    # Helper Function creating equations png files
    def createLatexFormula(self, formula, savedir, dpi):
        fig = pylab.figure()
        text = fig.text(0, 0, formula)
        
        # Saving the figure will render the text.
        fig.savefig(savedir, dpi=dpi)
        
        # Now we can work with text's bounding box.
        bbox = text.get_window_extent()
        width, height = bbox.size / float(dpi) + 0.005
        # Adjust the figure size so it can hold the entire text.
        fig.set_size_inches((width, height))

        # Adjust text's vertical position.
        dy = (bbox.ymin/float(dpi))/height
        text.set_position((0, -dy))

        # Save the adjusted text.
        fig.savefig(savedir, dpi=dpi)
        pyplot.close(fig)
