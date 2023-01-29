import pytest

def test_basic1():
    a = 1
    b = 2
    assert a + 1 == b, 'test failed'
    assert a == b, 'test failed as a is not equal b'

def test_basic2():
    name = 'selenium'
    assert name.upper() == 'SELENIUM'

