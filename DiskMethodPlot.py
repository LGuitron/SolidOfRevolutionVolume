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
        
        # Force a minimum of 1 disk
        if(parent.input_section.text()=='' or int(parent.input_section.text())==0):
            disks = 1
        else:
            disks = int(parent.input_section.text())
        
        self.diskAmount  = disks
        self.solidVolume = 0        # Calculate Volume by summing volume of each disk
        self.startX      = 0
        self.endX        = 2
        
        fig = Figure()
        #fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        u = np.linspace(self.startX, self.endX, 60)
        self.v = np.linspace(0, 2*np.pi, 60)
        self.plot()
        
    def plot(self):
        
        mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
        d = mathFunction.f_params_dict
        
        # Calculate X coordinate difference of rectangles
        deltaX = (self.endX - self.startX)/self.diskAmount
        
        for i in range(self.diskAmount):
            
            # Calculate function value at midpoint
            midpoint = i*deltaX + 0.5*deltaX
            

            x_mid       = np.linspace(midpoint, midpoint, 60)          # All X values fixed to midpoint
            x_range     = np.linspace(i*deltaX , (i+1)*deltaX, 60)     # X range for this cylinder
            
            X_mid, V   = np.meshgrid(x_mid, self.v)
            X_range, V = np.meshgrid(x_range, self.v)

            if(mathFunction.f_type == "polinomial"):
                Y = (float(d['A'])*X_mid**3 + float(d['B'])*X_mid**2 + float(d['C'])*X_mid + float(d['D'])) * np.cos(V)
                Z = (float(d['A'])*X_mid**3 + float(d['B'])*X_mid**2 + float(d['C'])*X_mid + float(d['D'])) * np.sin(V)

            self.ax.plot_surface(X_range, Y, Z, alpha=0.3, color='red', rstride=6, cstride=12)
            
            # Calculate volume of current cylinder
            radius = (float(d['A'])*midpoint**3 + float(d['B'])*midpoint**2 + float(d['C'])*midpoint + float(d['D']))
            diskVolume = deltaX*math.pi*radius**2
            self.solidVolume += diskVolume
