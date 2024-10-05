import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)

def test_last_calculation(calculator):
    calculator.add(1, 2)
    assert calculator.get_last_calculation() == 3

def test_clear_history(calculator):
    calculator.add(1, 2)
    calculator.clear_history()
    assert calculator.get_last_calculation() is None
