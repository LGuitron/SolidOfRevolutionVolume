from PyQt5.QtWidgets import QWidget, QVBoxLayout
from GlobalVariables import GlobalVariables
from SolidRevPlot import SolidRevPlot

class SolidRevWidget(QWidget):
 
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.m = None
        
    # Update plot whenever a new function is selected
    def updatePlot(self):
        
        if(self.m != None):
            self.layout.removeWidget(self.m)
        
        self.m = SolidRevPlot(self)
        self.layout.addWidget(self.m)
        self.setLayout(self.layout)
'''
class SolidRevWidget(FigureCanvas):

    def __init__(self, parent=None):
        
        fig = Figure()
        #fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        u = np.linspace(0, 2, 60)
        v = np.linspace(0, 2*np.pi, 60)
        U, V = np.meshgrid(u, v)

    def plot(self)
        X = U
        
        if(mathFunction.f_type == "polinomial"):
            Y = (float(d['A'])*x**3 + float(d['B'])*x**2 + float(d['C'])*x + float(d['D'])) * np.cos(V)
            Z = (float(d['A'])*x**3 + float(d['B'])*x**2 + float(d['C'])*x + float(d['D'])) * np.sin(V)
        
        #Y = X * np.cos(V)
        #Z = X * np.sin(V)
        ax.plot_surface(X, Y, Z, alpha=0.3, color='blue', rstride=6, cstride=12)
        plt.show()
'''
        
