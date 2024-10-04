from abc import ABC, abstractmethod
from typing import Dict, Type
from app.operations import Addition, Subtraction, Multiplication, Division
from typing import Union, List, Dict, Type

class Calculation(ABC):
    @abstractmethod
    def compute(self, a: float, b: float) -> float:
        pass


class Calculator:
    operations_map: Dict[str, Type[Calculation]] = {
        'add': Addition,
        'subtract': Subtraction,
        'multiply': Multiplication,
        'divide': Division,
    }

    def __init__(self) -> None:
        self.history: List[str] = []

    @classmethod
    def create(cls, operation: str) -> Union[Calculation, None]:
        return cls.operations_map.get(operation)()

    def calculate(self, operation: str, a: float, b: float) -> float:
        op = self.create(operation)
        result = op.compute(a, b)
        self.history.append(f"{operation}({a}, {b}) = {result}")
        return result

    def get_last_calculation(self) -> str:
        return self.history[-1] if self.history else "No calculations yet."


def main():
    calculator = Calculator()
    while True:
        user_input = input("Enter operation (add, subtract, multiply, divide) and two numbers (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Please enter an operation followed by two numbers.")
            continue
        operation, a_str, b_str = parts
        try:
            a, b = float(a_str), float(b_str)
            result = calculator.calculate(operation, a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid number. Please enter numeric values.")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
