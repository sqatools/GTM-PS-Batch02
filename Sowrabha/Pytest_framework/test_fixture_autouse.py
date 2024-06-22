import pytest
@pytest.fixture(scope="function",autouse=True)
def setup():
    print("__________Execution started________________")
    yield
    print("__________execution stopped_______")

def test_add():
    a=10
    b=20
    assert a+b==30

def test_sub():
    a=30
    b=20
    assert a-b==100


