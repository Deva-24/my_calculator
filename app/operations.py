# app/operations.py
from .operations_base import Addition, Subtraction, Multiplication, Division
from app.calculator import Calculation


# In app/operations.py

class Addition(Calculation):
    def __init__(self, a, b):
        super().__init__('add', (a, b))

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
