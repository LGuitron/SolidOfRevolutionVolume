from PyQt5.QtWidgets import QWidget, QTabWidget,QVBoxLayout, QListWidget, QCheckBox, QButtonGroup
from AddFunctionWidget import AddFunctionWidget
from FunctionPlotWidget import FunctionPlotWidget
from SolidRevWidget import SolidRevWidget
from CalculateVolumeWidget import CalculateVolumeWidget
from GlobalVariables import GlobalVariables


class MainTableWidget(QWidget):        
 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        
        self.layout = QVBoxLayout(self)
        self.layout.setDirection(QVBoxLayout.Direction.LeftToRight)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = AddFunctionWidget(self)
        self.tab2 = FunctionPlotWidget(self)
        self.tab3 = SolidRevWidget(self)
        self.tab4 = CalculateVolumeWidget(self)
        
        # Array of indices of tabs with plots (for making updates when switching to them)
        self.tabsWithPlots = [1,2,3]
        
        # Function whenever a new tab is clicked
        self.tabs.currentChanged.connect(self.updatePlot)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Agrega Funciones")
        self.tabs.addTab(self.tab2,"Ver Función")
        self.tabs.addTab(self.tab3,"Ver Sólido de Revolución")
        self.tabs.addTab(self.tab4,"Cálculo de Volumen")
        
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        
        # Objects changing when adding new math functions
        self.listWidget = None
        self.checkBoxLayout = QVBoxLayout()
        self.checkBoxGroup = QButtonGroup()
        self.updateListWidget()
    
    # Function for updatting math functions widget when new functions are added
    def updateListWidget(self, addCheckBox = False):
        
        # Delete existing layouts
        if(self.listWidget != None):
            self.layout.removeWidget(self.listWidget)
        
        # Delete existing layouts
        if(self.checkBoxLayout != None):
            self.layout.removeItem(self.checkBoxLayout)
        
        # Add list of math functions on the right side
        self.listWidget = QListWidget()
        
        stringMathFunctions = []
        
        i = 0
        for mathFunction in GlobalVariables.mathFunctionsList:
            i += 1
            stringMathFunctions.append(str(i) + ". " + str(mathFunction))

        self.listWidget.addItems(stringMathFunctions)
        self.listWidget.setMaximumWidth(0.3 * GlobalVariables.screenWidth)
        
        self.layout.addWidget(self.listWidget)
        
        
        if(addCheckBox):
            listLength = len(GlobalVariables.mathFunctionsList)
            newCheckBox = QCheckBox(str(listLength))
            self.checkBoxLayout.addWidget(newCheckBox)
            
            # Set the first function added to ON
            if(listLength==1):
                newCheckBox.setChecked(True)
                GlobalVariables.selectedIndex = 0

            newCheckBox.released.connect(self.selectFunction)
            self.checkBoxGroup.addButton(newCheckBox, listLength - 1)
            
        self.layout.addLayout(self.checkBoxLayout)
        self.setLayout(self.layout)
        
    # Function to set index of the selected function
    def selectFunction(self):
        GlobalVariables.selectedIndex = self.checkBoxGroup.checkedId()
        if(self.tabs.currentIndex() in self.tabsWithPlots):
            self.tabs.currentWidget().updatePlot()

    # Function to update Plot of the current tab (must have at least one function added)
    def updatePlot(self, index):
        #print("LEN: ", len(index))
        if(index in self.tabsWithPlots and GlobalVariables.selectedIndex != -1):
            self.tabs.widget(index).updatePlot()
