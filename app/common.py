

# app/common.py
from abc import ABC, abstractmethod

class Calculation(ABC):
    @abstractmethod
    def compute(self, a: float, b: float) -> float:
        pass
