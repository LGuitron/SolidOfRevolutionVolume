# Class for storing math function information
class MathFunction:

    def __init__(self, f_expression, x0, x1):
        self.f_expression = f_expression
        self.x0 = x0
        self.x1 = x1
        
    def __str__(self):
        return "f(x) = "+ str(self.f_expression) + "               x in (" + str(self.x0) + ", " + str(self.x1) +")"
