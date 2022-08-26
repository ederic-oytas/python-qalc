from abc import abstractmethod
from dataclasses import dataclass
from typing import Any


class Expression:
    """Abstract base class for all expressions in qalc."""

    @abstractmethod
    def evaluate(self) -> Any:
        """Return the value of this expression."""


@dataclass
class Addition(Expression):
    """Represents an addition operation (+)."""
    left: Expression
    right: Expression
    
    def evaluate(self) -> Any:
        return self.left.evaluate() + self.right.evaluate()


@dataclass
class Number(Expression):
    """Represents a number in qalc."""
    value: float
    
    def evaluate(self) -> float:
        return self.value
