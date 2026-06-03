import pytest
from calculator.calc import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0

def test_subtract():
    assert Calculator.subtract(10, 5) == 5

def test_multiply():
    assert Calculator.multiply(4, 3) == 12

def test_divide():
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)

def test_power():
    assert Calculator.power(2, 3) == 8
