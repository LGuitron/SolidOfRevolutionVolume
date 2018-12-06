# Class for storing math function information
class MathFunction:
    # f_type : {polinomial, trigonometric, exponential} 
    def __init__(self, f_type, f_params_dict):
        self.f_type = f_type
        self.f_params_dict = f_params_dict
        
    def __str__(self):
        
        retStr = ""
        if(self.f_type == "polinomial"):
            retStr = "f(x) = " + self.f_params_dict['A'] + "x^3 + " + self.f_params_dict['B'] + "x^2 + " + self.f_params_dict['C'] + "x + " + self.f_params_dict['D']
        return retStr
