from PyQt5.QtWidgets import QLineEdit, QLabel, QVBoxLayout

# FUNCTIONS FOR CREATING FORM PARAMETERS EASILY
def addParameters(layout, validator, defaultStr, parameterArray, inputSections):
    for parameter in parameterArray:
        label = QLabel()
        label.setText(parameter + " =")
        
        input_section = QLineEdit()
        input_section.setValidator(validator)
        input_section.setText(defaultStr)
        inputSections.append(input_section)

        layoutA = QVBoxLayout()
        layoutA.setDirection(QVBoxLayout.Direction.LeftToRight)
        layoutA.addWidget(label)
        layoutA.addWidget(input_section)
        layout.addLayout(layoutA)
