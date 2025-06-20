import pytest


@pytest.fixture(scope="function")
def setup():
    print("________________Execution started------------------------")
    yield
    print("--------------Testing done_______________")

def test_add(setup):
    a=8
    b=10
    assert a+b==18

def test_sub(setup):
    a=90
    b=78
    assert  a-b==12

#command to run fixture: python -m pytest -v -s .\test_fixture_basic.py
