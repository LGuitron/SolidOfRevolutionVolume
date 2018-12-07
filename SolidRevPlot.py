import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

from PyQt5.QtWidgets import QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from GlobalVariables import GlobalVariables

class SolidRevPlot(FigureCanvas):

    def __init__(self, parent=None):
        
        fig = Figure()
        #fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
            
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        u = np.linspace(0, 2, 60)
        v = np.linspace(0, 2*np.pi, 60)
        self.U, self.V = np.meshgrid(u, v)
        self.plot()
        
    def plot(self):
        
        X = self.U
        
        mathFunction = GlobalVariables.mathFunctionsList[GlobalVariables.selectedIndex]
        d = mathFunction.f_params_dict
        
        if(mathFunction.f_type == "polinomial"):
            Y = (float(d['A'])*X**3 + float(d['B'])*X**2 + float(d['C'])*X + float(d['D'])) * np.cos(self.V)
            Z = (float(d['A'])*X**3 + float(d['B'])*X**2 + float(d['C'])*X + float(d['D'])) * np.sin(self.V)

        self.ax.plot_surface(X, Y, Z, alpha=0.3, color='blue', rstride=6, cstride=12)
        plt.show()
