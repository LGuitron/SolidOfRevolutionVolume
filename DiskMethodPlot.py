from PyQt5.QtWidgets import QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d

class DiskMethodPlot(FigureCanvas, QWidget):

    def __init__(self, parent=None):
        
        X = parent.X
        Y = parent.Y
        Z = parent.Z
        
        fig = Figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


        for i in range(parent.displayedDisks):
            self.ax.plot_surface(X[i], Y[i], Z[i], alpha=0.3, color='red', rstride=6, cstride=12)
