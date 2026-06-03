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

    @staticmethod
    def factorial(n):
        
        if n < 0:
            raise ValueError("Факториал не определен для отрицательных чисел")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
