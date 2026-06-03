class Calculator:
    """Простой калькулятор с базовыми операциями"""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Нельзя делить на ноль!")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
