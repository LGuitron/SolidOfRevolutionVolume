from sympy import var
import numpy as np
from GlobalVariables import GlobalVariables

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Function for plotting 2D function
class Plot2D(FigureCanvas):
    
    def __init__(self, parent=None):
        fig = Figure()
        
        self.function_points = 200
        
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

        x0 = mathFunction[0].x0
        x1 = mathFunction[len(mathFunction)-1].x1

        x = np.linspace(x0, x1, self.function_points)
        y = np.zeros(self.function_points)

        for i in range(self.function_points):
            
            # Iterate through the math function to get the part corresponding to the point to be evaluated
            for part in mathFunction:
                if(part.x0 <= x[i] and x[i] <= part.x1):
                    currentPart = part
                    break
            y[i] = currentPart.f_expression.subs(var('x'), x[i])
            
        ax = self.figure.add_subplot(111)
        ax.plot(x,y,'r-')
        title = ""
        for part in mathFunction:
            title += str(part) + "\n"
        ax.set_title(title)    
