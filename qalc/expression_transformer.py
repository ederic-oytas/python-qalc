from decimal import Decimal
from .expression import Addition, Division, Multiplication, Number, Subtraction

import lark



@lark.v_args(inline=True)
class ExpressionTransformer(lark.Transformer):
    
    add = Addition
    sub = Subtraction
    mul = Multiplication
    div = Division
    
    def number(self, value_token: lark.Token) -> Number:
        return Number(Decimal(value_token))
    
    
