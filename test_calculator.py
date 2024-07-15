# test_calculator.py
import pytest
from Calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(-1, -1) == -2

def test_subtract():
    assert Calculator.subtract(10, 5) == 5
    assert Calculator.subtract(-1, 1) == -2
    assert Calculator.subtract(-1, -1) == 0

def test_multiply():
    assert Calculator.multiply(3, 7) == 21
    assert Calculator.multiply(-1, 1) == -1
    assert Calculator.multiply(-1, -1) == 1

def test_divide():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(-1, 1) == -1
    assert Calculator.divide(-1, -1) == 1
    with pytest.raises(ValueError):
        Calculator.divide(20, 0)