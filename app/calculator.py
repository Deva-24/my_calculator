from typing import List, Union

class Calculator:
    history: List[Union[int, float]] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator.history.append(result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator.history.append(result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append(result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator.history.append(result)
        return result

    @classmethod
    def get_last_calculation(cls) -> Union[int, float, None]:
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()


class Calculation:
    def __init__(self, operation, operands):
        self.operation = operation
        self.operands = operands
    
    def perform(self):
        return self.operation(*self.operands)

__all__ = ['Calculation']
