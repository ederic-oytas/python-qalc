from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
import operator
from typing import Any, Callable, ClassVar


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
    operation: ClassVar[Callable[[Any, Any], Any]]
    
    def evaluate(self) -> Any:
        return self.operation(self.left.evaluate(), self.right.evaluate())
    
    def display_str(self) -> str:
        """Return a display string of this expression."""
        return f"({self.left.display_str()} {self.symbol} {self.right.display_str()})"

class Addition(BinaryInfixOperation):
    """Represents an addition operation (+)."""
    symbol = '+'
    operation = operator.add


class Subtraction(BinaryInfixOperation):
    """Represents a subtraction operation (-)."""
    symbol = '-'
    operation = operator.sub


class Multiplication(BinaryInfixOperation):
    """Represents a multiplication operation (*)."""
    symbol = '*'
    operation = operator.mul
    

class Division(BinaryInfixOperation):
    """Represents a division operation (/)."""
    symbol = '/'
    operation = operator.truediv


@dataclass
class Number(Expression):
    """Represents a number in qalc."""
    value: Decimal
    
    def evaluate(self) -> Decimal:
        return self.value
    
    def display_str(self) -> str:
        return f"{self.value}"
