import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_calculate_addition(calculator):
    result = calculator.calculate('add', 1, 2)
    assert result == 3
    assert calculator.get_last_calculation() == "add(1.0, 2.0) = 3.0"

def test_calculate_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.calculate('divide', 1, 0)

def test_get_last_calculation(calculator):
    calculator.calculate('subtract', 5, 3)
    assert calculator.get_last_calculation() == "subtract(5.0, 3.0) = 2.0"
