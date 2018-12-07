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
        
        self.function_points = 100
        
        fig = Figure()
        #fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
            
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        self.u = np.linspace(GlobalVariables.x0, GlobalVariables.x1, self.function_points)
        v = np.linspace(0, 2*np.pi, self.function_points)
        self.U, self.V = np.meshgrid(self.u, v)
        self.plot()
        
    def plot(self):
        
        X = self.U        
        mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]

            
        # Get value of function for each of the points specified in u
        f_vals = np.zeros(self.function_points)
        F_vals = np.zeros((self.function_points, self.function_points))
        
        for i in range(self.function_points):
            f_vals[i] = mathFunction.f_expression.subs(var('x'), self.u[i])
        
        for i in range(len(F_vals)):
            F_vals[i] = f_vals
        
        Y = F_vals * np.cos(self.V)
        Z = F_vals * np.sin(self.V)
            

        self.ax.plot_surface(X, Y, Z, alpha=0.3, color='blue', rstride=6, cstride=12)
        plt.show()
