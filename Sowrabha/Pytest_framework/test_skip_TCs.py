import pytest


@pytest.mark.smoke
def test_add():
    a=110
    b=10
    assert a+b==120

@pytest.mark.sanity
def test_add2():
    a = 110
    b = 100
    assert a + b == 210

@pytest.mark.smoke
def test_add3():
    a=10
    b=10
    assert a+b==120

@pytest.mark.sanity
def test_add4():
    a=102
    b=108
    assert a+b==210





