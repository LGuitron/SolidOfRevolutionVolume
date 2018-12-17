# Overview

This repository provides code for visualizing solids of revolution generated
by rotating an R2 function around the x axis, as well as the volume calcuation of 
with definite integrals, and an approximation with the Disk Method.
The user can interact with the program with a PyQt5 GUI.

## Dependencies

* sympy
* numpy
* PyQt5
* matplotlib


## User Input

The program accepts functions by parts as input for generating solids of revolution, 
each of the parts of a function require the function expression, as well as its interval 
(floating point numbers between -999,999.999 and 999,999.999).

Valid function expressions only have a single variable "x", and are valid expressions according to the sympy library. 
https://docs.sympy.org/


### Input Example

After adding a function expression after the "f(x)" label as well as the interval of the function
click on the button "Agregar nueva parte", if the inputs are valid the interpreted expression will be
displayed below the label "Función Actual".

![alt text](https://github.com/LGuitron/SolidOfRevolutionVolume/blob/master/images/InputExample1.png)

After adding all the function's parts click on the button "Aceptar", the function will be displayed on a
table in the right.

![alt text](https://github.com/LGuitron/SolidOfRevolutionVolume/blob/master/images/InputExample2.png)


## 2D Plot and Solid of Revolution

After a function has been added the user may see its corresponding 2D plot and solid of revoltion in the corresponding tabs.
If new functions are added, the user can select the function to be displayed using the checkboxes that correspond
to each function on the right side of the screen.

![alt text](https://github.com/LGuitron/SolidOfRevolutionVolume/blob/master/images/2Dplot.png)

In the solid of revolution tab the user can open an interactive graph by clicking on "Abrir gráfica interactiva"

![alt text](https://github.com/LGuitron/SolidOfRevolutionVolume/blob/master/images/sorPlot.png)


## Volme Calculation

The repository also includes two methods for calculating the volume of each solid of revolution:

### Disk Method

This method makes an approximation of the solid's volume by dividing it into various cylinders and adding
up the volume of each cylinder.
The user may add a number of cylinders between 1 and 999,999 for volume calculations, and a plot displayed
below will display a maximum of 200 cylinders.

![alt text](https://github.com/LGuitron/SolidOfRevolutionVolume/blob/master/images/approxPlot.png)

### Definite Integral

This option will display the operations performed in order to calculate the solid's volume using definite integrals.

![alt text](https://github.com/LGuitron/SolidOfRevolutionVolume/blob/master/images/integral.png)
