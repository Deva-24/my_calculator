# app/operations_base.py
from abc import ABC, abstractmethod


# In app/calculator.py

class Calculation:
    def __init__(self, operation, operands):
        self.operation = operation
        self.operands = operands

    def compute(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    # In app/operations.py

from app.calculator import Calculation

class Addition(Calculation):
    def __init__(self, a, b):
        super().__init__('add', (a, b))  # Pass 'add' as the operation and (a, b) as operands

    def compute(self):
        return sum(self.operands)

class Subtraction(Calculation):
    def __init__(self, a, b):
        super().__init__('subtract', (a, b))

    def compute(self):
        return self.operands[0] - self.operands[1]

class Multiplication(Calculation):
    def __init__(self, a, b):
        super().__init__('multiply', (a, b))

    def compute(self):
        return self.operands[0] * self.operands[1]

class Division(Calculation):
    def __init__(self, a, b):
        super().__init__('divide', (a, b))

    def compute(self):
        if self.operands[1] == 0:
            raise ValueError("Cannot divide by zero")
        return self.operands[0] / self.operands[1]

