from sympy import var
from sympy import lambdify
import numpy as np
import datetime

# Calculate X, Y, and Z coordinates for solid of revolution
def calculateCoordinatesSolidRev(mathFunction, function_circle_points, function_x_points):

    x0 = mathFunction[0].x0
    x1 = mathFunction[len(mathFunction)-1].x1
    
    u = np.linspace(x0, x1, function_x_points)
    v = np.linspace(0, 2*np.pi, function_circle_points)
    
    U, V = np.meshgrid(u, v)
    
    f_vals = np.zeros(function_x_points)
    F_vals = np.zeros((function_circle_points, function_x_points))

    for i in range(function_x_points):
        
        # Iterate through the math function to get the part corresponding to the point to be evaluated
        for part in mathFunction:
            if(part.x0 <= u[i] and u[i] <= part.x1):
                currentPart = part
                break
        f_vals[i] = currentPart.f_expression.subs(var('x'), u[i])
    
    for i in range(len(F_vals)):
        F_vals[i] = f_vals
    
    Y = F_vals * np.cos(V)
    Z = F_vals * np.sin(V)
    
    return U, Y, Z



# Calculate X, Y, and Z coordinates to be plotted
# Disk amount is the amount of disks to be displayed
def calculateCoordinates(mathFunction, diskAmount, function_circle_points, function_x_points):

    v = np.linspace(0, 2*np.pi, function_circle_points)
    x0 = mathFunction[0].x0
    x1 = mathFunction[len(mathFunction)-1].x1
    deltaX = (x1 - x0)/diskAmount                                                           # Calculate X coordinate difference of cylinders
    
    X = np.zeros((diskAmount,function_circle_points,function_x_points))
    Y = np.zeros((diskAmount,function_circle_points,function_x_points))
    Z = np.zeros((diskAmount,function_circle_points,function_x_points))

    currentIndex = 0

    # Calculate X values with subranges of each cylinder divided by the amount of function_points
    for i in range(diskAmount):
        x_range     = np.linspace(i*deltaX , (i+1)*deltaX, function_x_points)               # X range for this cylinder
        X_range, V  = np.meshgrid(x_range, v)
        X[i] = X_range
    
    currentIndex = 0
    
    # Store this value to set x1 of last part as x0 of next part
    x0_part = mathFunction[0].x0
    
    # Create Lambda Expressions for each function part and evaluate corresponding points
    for part in mathFunction:

        x_values = np.arange(part.x0 + 0.5*deltaX, part.x1 - 0.5*deltaX, deltaX)
        x_amount = len(x_values)
        f        = lambdify("x", part.f_expression, "numpy")
        f_eval   = f(x_values)
        
        if not isinstance(f_eval, (list,)):
            f_eval = np.full(x_amount, f_eval)

        for i in range(x_amount):
            F_vals              = np.full((function_circle_points,function_x_points), f_eval[i])    
            Y[currentIndex + i] = F_vals * np.cos(V)
            Z[currentIndex + i] = F_vals * np.sin(V)
        currentIndex += x_amount

    return X, Y, Z


# Calculate volume given number of disks
def calculateVolume(mathFunction, diskAmount):

    x0 = mathFunction[0].x0
    x1 = mathFunction[len(mathFunction)-1].x1
    deltaX = (x1 - x0)/diskAmount                                                # Calculate X coordinate difference of cylinders
    volumeApproximation = 0

    # Create Lambda Expressions for each function part and evaluate corresponding points
    for part in mathFunction:
        
        x_values = np.arange(part.x0 + 0.5*deltaX, part.x1, deltaX)
        x_amount = len(x_values)
        f        = lambdify("x", part.f_expression, "numpy")
        
        values   = f(x_values)
        if not isinstance(values, (list,)):
            values = np.full(x_amount, values)
        volumeApproximation  += np.sum(values**2)

    volumeApproximation *= np.pi*deltaX
    return volumeApproximation
