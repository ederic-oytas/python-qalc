

from qalc.expression import Number


def test_number():
    for i in [0.0, 1.0, 5.5, 100.0, 3.1, 3.2]:
        number = Number(i)
        assert number.evaluate() == i
