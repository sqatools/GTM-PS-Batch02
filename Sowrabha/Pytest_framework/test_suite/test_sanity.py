import pytest


@pytest.fixture(scope="function")

@pytest.mark.sanity
def test_five():
    a=2
    b=5
    assert a*b==10
@pytest.mark.smoke
def test_values():
    a=10
    b=5
    c=2
    assert a+b-c==13

