

from qalc.expression import Addition, Number


def test_number():
    for i in [0.0, 1.0, 5.5, 100.0, 3.1, 3.2]:
        number = Number(i)
        assert number.evaluate() == i


def test_addition():
    A = Addition
    N = Number
    
    assert A(N(1.0), N(2.5)).evaluate() == 3.5
    assert A(A(N(5.0), N(3.0)), N(10.5)).evaluate() == 18.5
    assert A(A(N(5.0), N(3.0)), A(N(10.5), N(10.5))).evaluate() == 29.0
