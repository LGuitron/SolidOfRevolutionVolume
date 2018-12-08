from sympy import var
import numpy as np
from GlobalVariables import GlobalVariables

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from PyQt5.QtWidgets import QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class SolidRevPlot(FigureCanvas):

    def __init__(self, parent=None):
        
        self.function_points = 500
        
        fig = Figure()
        #fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')

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
        
        self.u = np.linspace(x0, x1, self.function_points)
        v = np.linspace(0, 2*np.pi, self.function_points)
        self.U, self.V = np.meshgrid(self.u, v)
        X = self.U
            
        # Get value of function for each of the points specified in u
        f_vals = np.zeros(self.function_points)
        F_vals = np.zeros((self.function_points, self.function_points))
        
        for i in range(self.function_points):
            
            # Iterate through the math function to get the part corresponding to the point to be evaluated
            for part in mathFunction:
                if(part.x0 <= self.u[i] and self.u[i] <= part.x1):
                    currentPart = part
                    break
            f_vals[i] = currentPart.f_expression.subs(var('x'), self.u[i])
        
        for i in range(len(F_vals)):
            F_vals[i] = f_vals
        
        Y = F_vals * np.cos(self.V)
        Z = F_vals * np.sin(self.V)
            

        self.ax.plot_surface(X, Y, Z, alpha=0.3, color='blue', rstride=6, cstride=12)
        plt.show()
