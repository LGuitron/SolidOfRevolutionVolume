# Overview

This repository provides code for visualizing solids of revolution generated
by rotating an R2 function around the x axis, the user can interact with the 
generated plots throught a PyQt5 GUI.


## Dependencies

* sympy
* numpy
* PyQt5
* matplotlib


## User Input

The program accepts functions by parts as input for generating solids of revolution, 
each of the parts of a function require the function expression, as well as its interval 
(floating point numbers between -999,999.999 and 999,999.999).

Valid function expressions only have a single variable "x", and are expressions that can be
sympified with the sympy library. [https://docs.sympy.org/]


### Input Example





## Volme Calculation

The repository also includes two methods for calculating the volume of each solid of revolution:
* Disk Method
* Definite Integral
