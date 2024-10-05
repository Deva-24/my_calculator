# In tests/test_operations.py

import pytest
from app.operations import Addition, Subtraction, Multiplication, Division

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    addition = Addition(a, b)
    assert addition.compute() == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (0, 0, 0),
    (-1, -1, 0),
])
def test_subtraction(a, b, expected):
    subtraction = Subtraction(a, b)
    assert subtraction.compute() == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 10, 0),
    (-2, -3, 6),
])
def test_multiplication(a, b, expected):
    multiplication = Multiplication(a, b)
    assert multiplication.compute() == expected

def test_division():
    division = Division(10, 2)
    assert division.compute() == 5

    with pytest.raises(ValueError):
        division_by_zero = Division(10, 0)
        division_by_zero.compute()
