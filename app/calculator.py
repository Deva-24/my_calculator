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
