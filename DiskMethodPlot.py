from sympy import var

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import math

from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from GlobalVariables import GlobalVariables


class DiskMethodPlot(FigureCanvas, QWidget):

    def __init__(self, parent=None):
        
        self.function_points = 60
        
        # Force a minimum of 1 disk
        if(parent.input_section.text()=='' or int(parent.input_section.text())==0):
            disks = 1
        else:
            disks = int(parent.input_section.text())
        
        self.diskAmount  = disks
        self.solidVolume = 0        # Calculate Volume by summing volume of each disk
        
        fig = Figure()
        #fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.v = np.linspace(0, 2*np.pi, self.function_points)
        self.plot()
        
    def plot(self):

        mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
        
        x0 = mathFunction[0].x0
        x1 = mathFunction[len(mathFunction)-1].x1
        deltaX = (x1 - x0)/self.diskAmount                # Calculate X coordinate difference of rectangles
        
        for i in range(self.diskAmount):            
            # Calculate function value at midpoint
            midpoint = x0 + (i+0.5)*deltaX

            x_range     = np.linspace(i*deltaX , (i+1)*deltaX, self.function_points)      # X range for this cylinder
            X_range, V = np.meshgrid(x_range, self.v)

            # Iterate through the math function to get the part corresponding to the point to be evaluated
            for part in mathFunction:
                if(part.x0 <= midpoint and midpoint <= part.x1):
                    currentPart = part
                    break
            radius = currentPart.f_expression.subs(var('x'), midpoint)
            F_vals = np.full((self.function_points, self.function_points), float(radius))
            
            Y = F_vals * np.cos(V)
            Z = F_vals * np.sin(V)
                
            self.ax.plot_surface(X_range, Y, Z, alpha=0.3, color='red', rstride=6, cstride=12)
            
            # Calculate volume of current cylinder
            diskVolume = deltaX*math.pi*radius**2
            self.solidVolume += diskVolume
