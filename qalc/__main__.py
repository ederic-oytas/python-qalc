import argparse


def make_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'expr', metavar='EXPR', type=str,
        help='mathematical expression to evaluate',
    )
    
    return parser


def main() -> None:
    parser = make_arg_parser()
    args = parser.parse_args()
    expr: str = args.expr
    print(f'inputted: {expr}')


if __name__ == '__main__':
    main()
