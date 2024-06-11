import pytest
from calcify.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3
    assert add(1, 2, 3) == 6
    assert add(1, 2, 3.1, 4) == 10.1
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, 2) == -3
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(1, 2, 3.0) == 6.0
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(10, 5) == 2
    assert divide(1, 3) == 1/3
    with pytest.raises(ValueError):
        divide(1, 0)
