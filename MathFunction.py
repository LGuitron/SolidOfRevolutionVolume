# Class for storing math function information
class MathFunction:

    def __init__(self, f_expression):
        self.f_expression = f_expression

    def __str__(self):
        return "f(x) = "+ str(self.f_expression)
