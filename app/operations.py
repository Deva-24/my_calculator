from app.calculator import Calculation

class Addition(Calculation):
    def compute(self, a: float, b: float) -> float:
        return a + b

class Subtraction(Calculation):
    def compute(self, a: float, b: float) -> float:
        return a - b

class Multiplication(Calculation):
    def compute(self, a: float, b: float) -> float:
        return a * b

class Division(Calculation):
    def compute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
