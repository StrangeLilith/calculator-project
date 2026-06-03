import pytest
from calculator.advanced import AdvancedCalculator

def test_square_root():
    assert AdvancedCalculator.square_root(16) == 4

def test_square_root_negative():
    with pytest.raises(ValueError):
        AdvancedCalculator.square_root(-4)

def test_percentage():
    assert AdvancedCalculator.percentage(200, 15) == 30
