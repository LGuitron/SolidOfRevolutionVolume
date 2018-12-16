from PyQt5.QtWidgets import QWidget, QTabWidget,QVBoxLayout, QCheckBox, QButtonGroup, QLabel, QTableWidget, QHeaderView
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
from AddFunctionWidget import AddFunctionWidget
from FunctionPlotWidget import FunctionPlotWidget
from SolidRevWidget import SolidRevWidget
from CalculateVolumeWidget import CalculateVolumeWidget
from GlobalVariables import GlobalVariables
from sympy import latex
from LatexFormulas import createLatexFormula

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
        self.tableWidget  = None
        
        #self.checkBoxLayout = QVBoxLayout()
        self.checkBoxGroup = QButtonGroup()
        self.updateListWidget()
        
        # Function to be used for function titles
        self.functionTitleFont = QFont()
        self.functionTitleFont.setBold(True)
        self.functionTitleFont.setPointSize(14)
        
    # Function for updatting math functions widget when new functions are added
    def updateListWidget(self, addCheckBox = False):
    
        # Delete existing layouts
        if(self.tableWidget != None):
            self.layout.removeWidget(self.tableWidget)
        
        listLength = len(GlobalVariables.mathFunctionsList)
        # Row added for each function, and row added for each function part
        rowAmount = listLength
        
        for mathFunction in GlobalVariables.mathFunctionsList:
            rowAmount += len(mathFunction)
        
        
        self.tableWidget = QTableWidget(rowAmount, 3, self)
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
        rowIndex = 0
        for i in range(listLength):
            mathFunction = GlobalVariables.mathFunctionsList[i]
            
            rowLabel = QLabel()
            self.tableWidget.setSpan(rowIndex, 0, 1, 2)                      # Mix 2 columns for function title
            
            rowLabel.setText("Función " + str(i+1))
            rowLabel.setFont(self.functionTitleFont)
            rowLabel.setAlignment(Qt.AlignCenter)
            self.tableWidget.setCellWidget(rowIndex, 0, rowLabel)            # Add name of this function as a whole
            self.tableWidget.setSpan(rowIndex, 2, len(mathFunction) + 1, 1)  # Mix rows depending on number of parts of this function
            
            # Add Checkbox for this function
            newCheckBox = QCheckBox("F" + str(i+1))
            newCheckBox.released.connect(self.selectFunction)
            
            # Set first checkbox to be on
            if(listLength==1):
                newCheckBox.setChecked(True)
                GlobalVariables.selectedIndex = 0
            
            # Set the currently selected Checkbox
            if(GlobalVariables.selectedIndex == i):
                newCheckBox.setChecked(True)
                
            self.tableWidget.setCellWidget(rowIndex, 2, newCheckBox)
            self.checkBoxGroup.addButton(newCheckBox, i)
            
                                                                             
            rowIndex += 1

            for j in range(rowIndex, rowIndex + len(mathFunction)):
                part = mathFunction[j-rowIndex]
                createLatexFormula(r'$f(x) = '+ latex(part.f_expression) +'$', 'equations/function_part_' + str(j), 90)
                createLatexFormula(r'$ x \in ('+str(part.x0)+', '+str(part.x1)+')$', 'equations/interval_' + str(j), 90)
                
                partLabel = QLabel()
                partLabel.setPixmap(QPixmap('equations/function_part_' + str(j)))
                self.tableWidget.setCellWidget(j, 0, partLabel)
                
                partInterval = QLabel()
                partInterval.setPixmap(QPixmap('equations/interval_' + str(j)))
                self.tableWidget.setCellWidget(j, 1, partInterval)
                
            
            rowIndex += len(mathFunction)
            
        self.tableWidget.setMaximumWidth(0.4 * GlobalVariables.screenWidth)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)




    # Function to set index of the selected function
    def selectFunction(self):
        GlobalVariables.selectedIndex = self.checkBoxGroup.checkedId()
        if(self.tabs.currentIndex() in self.tabsWithPlots):
            self.tabs.currentWidget().updatePlot()

    # Function to update Plot of the current tab (must have at least one function added)
    def updatePlot(self, index):
        if(index in self.tabsWithPlots and GlobalVariables.selectedIndex != -1):
            self.tabs.widget(index).updatePlot()
