from sympy import var
import numpy as np

# Calculate X, Y, and Z coordinates for solid of revolution
def calculateCoordinatesSolidRev(mathFunction, function_points):

    x0 = mathFunction[0].x0
    x1 = mathFunction[len(mathFunction)-1].x1
        
    u = np.linspace(x0, x1, function_points)
    v = np.linspace(0, 2*np.pi, function_points)
    U, V = np.meshgrid(u, v)

    # Get value of function for each of the points specified in u
    f_vals = np.zeros(function_points)
    F_vals = np.zeros((function_points, function_points))
    
    for i in range(function_points):
        
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
def calculateCoordinates(mathFunction, diskAmount, function_points):

    v = np.linspace(0, 2*np.pi, function_points)
    x0 = mathFunction[0].x0
    x1 = mathFunction[len(mathFunction)-1].x1
    deltaX = (x1 - x0)/diskAmount                                                # Calculate X coordinate difference of cylinders
    
    X = np.zeros((diskAmount,function_points,function_points))
    Y = np.zeros((diskAmount,function_points,function_points))
    Z = np.zeros((diskAmount,function_points,function_points))
    
    # Display max amount of disks or disks introduced by user
    for i in range(diskAmount):

        midpoint    = x0 + (i+0.5)*deltaX                                            # Calculate function value at midpoint
        x_range     = np.linspace(i*deltaX , (i+1)*deltaX, function_points)  # X range for this cylinder
        X_range, V  = np.meshgrid(x_range, v)

        # Iterate through the math function to get the part corresponding to the point to be evaluated
        for part in mathFunction:
            if(part.x0 <= midpoint and midpoint <= part.x1):
                currentPart = part
                break
        radius = currentPart.f_expression.subs(var('x'), midpoint)
        F_vals = np.full((function_points, function_points), float(radius))
        
        X[i] = X_range
        Y[i] = F_vals * np.cos(V)
        Z[i] = F_vals * np.sin(V)
    
    return X, Y, Z 


# Calculate volume given number of disks
def calculateVolume(mathFunction, diskAmount):
    
    x0 = mathFunction[0].x0
    x1 = mathFunction[len(mathFunction)-1].x1
    deltaX = (x1 - x0)/diskAmount                                                # Calculate X coordinate difference of cylinders
    volumeApproximation = 0
    
    for i in range(diskAmount):
        
        midpoint = x0 + (i+0.5)*deltaX
        
        for part in mathFunction:
            if(part.x0 <= midpoint and midpoint <= part.x1):
                currentPart = part
                break
        
        radius = currentPart.f_expression.subs(var('x'), midpoint)
        volumeApproximation += radius**2
    volumeApproximation *= np.pi*deltaX
    return volumeApproximation
