from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, ClassVar, Literal


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
    
    associativity: ClassVar[Literal['left', 'right', 'neither']]
    symbol: ClassVar[str]
    precedence: ClassVar[int]
    
    def display_str(self) -> str:
        """Return a display string of this expression."""
        
        left = self.left
        left_s = left.display_str()
        if isinstance(left, BinaryInfixOperation):
            if left.precedence < self.precedence:
                left_s = f"({left_s})"
            elif (left.precedence == self.precedence
                    and left.associativity != 'left'):
                left_s = f"({left_s})"
        
        right = self.right
        right_s = right.display_str()
        if isinstance(right, BinaryInfixOperation):
            if right.precedence < self.precedence:
                right_s = f"({right_s})"
            elif (right.precedence == self.precedence
                    and right.associativity != 'right'):
                right_s = f"({right_s})"
        
        return f"{left_s} {self.symbol} {right_s}"


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
