import pytest
from app.operations import Addition, Subtraction, Multiplication, Division

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    assert Addition().compute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (0, 0, 0),
    (-1, -1, 0),
])
def test_subtraction(a, b, expected):
    assert Subtraction().compute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 10, 0),
    (-2, -3, 6),
])
def test_multiplication(a, b, expected):
    assert Multiplication().compute(a, b) == expected

def test_division():
    assert Division().compute(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        Division().compute(10, 0)
