from abc import ABC, abstractmethod
from typing import Dict, Type

class Calculation(ABC):
    @abstractmethod
    def compute(self, a: float, b: float) -> float:
        pass
