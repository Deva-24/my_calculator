from typing import List, Union, Callable

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    history: List[Union[int, float]] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of two numbers."""
        result = a + b
        Calculator.history.append(result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return the difference between two numbers."""
        result = a - b
        Calculator.history.append(result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Return the product of two numbers."""
        result = a * b
        Calculator.history.append(result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Return the quotient of two numbers. Raise ZeroDivisionError if dividing by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator.history.append(result)
        return result

    @classmethod
    def get_last_calculation(cls) -> Union[int, float, None]:
        """Return the last calculation result from history."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls) -> None:
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Union[int, float]]:
        """Return the history of calculations."""
        return cls.history


class Calculation:
    """A class to represent a calculation operation."""
    
    def __init__(self, operation: Callable, operands: List[float]):
        """Initialize the calculation with an operation and its operands."""
        self.operation = operation
        self.operands = operands
    
    def perform(self) -> Union[int, float]:
        """Perform the calculation using the provided operation and operands."""
        return self.operation(*self.operands)

__all__ = ['Calculation']
