from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, ClassVar, Literal, Union


class Expression(ABC):
    """Abstract base class for all expressions in qalc."""

    @abstractmethod
    def evaluate(self) -> Any:
        """Return the value of this expression."""
        
    @abstractmethod
    def display_str(self) -> str:
        """Return a display string of this expression."""


@dataclass
class BinaryInfixOperation(Expression):
    """Represents a binary infix operation (e.g. addition, subtraction)."""
    left: Expression
    right: Expression
    
    symbol: ClassVar[str]
    
    def display_str(self) -> str:
        """Return a display string of this expression."""
        return f"({self.left.display_str()} {self.symbol} {self.right.display_str()})"


@dataclass
class Addition(BinaryInfixOperation):
    """Represents an addition operation (+)."""
    left: Expression
    right: Expression
    
    associativity = 'left'
    symbol = '+'
    precedence = 1000
    
    def evaluate(self) -> Any:
        return self.left.evaluate() + self.right.evaluate()


@dataclass
class Number(Expression):
    """Represents a number in qalc."""
    value: float
    
    def evaluate(self) -> float:
        return self.value
    
    def display_str(self) -> str:
        return f"{self.value}"
