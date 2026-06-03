import math

class AdvancedCalculator:
    
    
    @staticmethod
    def square_root(x):
        if x < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа!")
        return math.sqrt(x)
    
    @staticmethod
    def percentage(value, percent):
        return value * (percent / 100)
