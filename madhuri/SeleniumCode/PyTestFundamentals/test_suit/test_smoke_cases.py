"""
command to install pytest

"""
import pytest


@pytest.mark.smoke
def test_function1():
    a = 50
    b = 60
    assert a + b == 110


@pytest.mark.smoke
def test_function2():
    a = 50
    b = 20
    assert a - b == 40


@pytest.mark.smoke
@pytest.mark.sanity
def test_function3():
    a = 50
    b = 3
    assert a * b == 150


@pytest.mark.sanity
def test_function4():
    a = 50
    b = 3
    assert a * b == 150


@pytest.mark.regression
def test_function5():
    a = 50
    b = 3
    assert a * b == 150


@pytest.mark.regression
def test_function6():
    a = 50
    b = 3
    assert a * b == 150
