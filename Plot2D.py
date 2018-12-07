from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from GlobalVariables import GlobalVariables

# Function for plotting 2D function
class Plot2D(FigureCanvas):
    
    def __init__(self, parent=None):
        fig = Figure()
        
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        
        mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
        d = mathFunction.f_params_dict
        
        x = np.linspace(GlobalVariables.x0, GlobalVariables.x1, 100)
        
        
        if(mathFunction.f_type == "polinomial"):
            y = float(d['A'])*x**3 + float(d['B'])*x**2 + float(d['C'])*x + float(d['D'])

        ax = self.figure.add_subplot(111)
        ax.plot(x,y,'r-')
        ax.set_title(str(mathFunction))    
