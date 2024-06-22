import pytest


@pytest.fixture(scope="module")
def setup():
    print("_________Execution started__________________")
    yield
    print("______________execution completed______________")

def test_add(setup):
    a=10
    b=20
    assert a+b==40

def test_sub(setup):
    a=25
    b=33
    assert b-a==8

def test_mul(setup):
    a=50
    b=5
    assert a*b==250


