import argparse
import lark
from qalc.expression import Expression

from qalc.expression_transformer import ExpressionTransformer


def make_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'expr', metavar='EXPR', type=str,
        help='mathematical expression to evaluate',
    )
    
    return parser


def make_lark_parser() -> lark.Lark:
    return lark.Lark.open(
        'qalc/grammar.lark',  # TODO reliably get this resource
        start='expr'
    )


def main() -> None:
    arg_parser = make_arg_parser()
    lark_parser = make_lark_parser()
    
    args = arg_parser.parse_args()
    expr_str: str = args.expr
    ast = lark_parser.parse(expr_str)
    
    transformer = ExpressionTransformer()
    expr: Expression = transformer.transform(ast)
    
    print()
    print(f"  {expr.display_str()}")
    print()
    print(expr.evaluate())
    print()


if __name__ == '__main__':
    main()
