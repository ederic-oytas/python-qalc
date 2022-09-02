from decimal import Decimal
from typing import Any, Callable
import operator
from qalc.expression import Addition, BinaryInfixOperation, Division, Multiplication, Number, Subtraction


def test_number():
    for a_s in ['0.0', '1.0', '5.5', '100.0', '3.1', '3.2']:
        number = Number(Decimal(a_s))
        assert number.evaluate() == Decimal(a_s)


class BinaryInfixOperationTests:
    
    expr_type: type[BinaryInfixOperation]
    operation: Callable[[Any, Any], Any]
    
    number_cases = [
        ('1.0', '2.5'),
        ('5.0', '3.0'),
        ('3049.5', '574.5'),
        ('1234895.35', '48234.5'),
        ('-1234895.35', '48234.5'),
        ('-1234895.35', '-48234.5'),
        ('1234895.35', '-48234.5'),
        ('32149.45', '1840.8021934')
    ]
    
    def test_evaluate(self):
        for a_s, b_s in self.number_cases:
            expr = self.expr_type(Number(Decimal(a_s)), Number(Decimal(b_s)))
            assert expr.evaluate() == self.operation(Decimal(a_s), Decimal(b_s))


class TestAddition(BinaryInfixOperationTests):
    expr_type = Addition
    operation = operator.add


class TestSubtraction(BinaryInfixOperationTests):
    expr_type = Subtraction
    operation = operator.sub


class TestMultiplication(BinaryInfixOperationTests):
    expr_type = Multiplication
    operation = operator.mul
    
    
class TestDivision(BinaryInfixOperationTests):
    expr_type = Division
    operation = operator.truediv
