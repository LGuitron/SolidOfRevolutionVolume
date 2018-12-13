import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget
from mpl_toolkits.mplot3d import axes3d

class SolidRevInteractivePlot(QWidget):

    def __init__(self, parent=None):
    
        super(QWidget, self).__init__(parent)

        X = parent.X
        Y = parent.Y
        Z = parent.Z

        fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1, projection='3d')

        self.ax.plot_surface(X, Y, Z, alpha=0.3, color='blue', rstride=6, cstride=12)
        plt.show()
