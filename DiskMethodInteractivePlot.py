import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget
from mpl_toolkits.mplot3d import axes3d

class DiskMethodInteractivePlot(QWidget):

    def __init__(self, parent=None):
        
        super(QWidget, self).__init__(parent)

        X = parent.X
        Y = parent.Y
        Z = parent.Z

        fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')

        for i in range(parent.displayedDisks):
            self.ax.plot_surface(X[i], Y[i], Z[i], alpha=0.3, color='red', rstride=6, cstride=12)
        plt.show()
