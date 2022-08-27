from .expression import Addition, Number

import lark



@lark.v_args(inline=True)
class ExpressionTransformer(lark.Transformer):
    
    def add(self, left, right):
        return Addition(left, right)
    
    def number(self, value_token: lark.Token) -> Number:
        return Number(float(value_token))
    
    
