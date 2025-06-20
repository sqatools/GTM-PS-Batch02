"""
command to install pytest

"""
import pytest
from test_data import *


@pytest.mark.smoke
@pytest.mark.xfail
def test_function1():
    a = 50
    b = 60
    assert a + b == 110


@pytest.mark.smoke
@pytest.mark.xfail
def test_function2():
    a = 50
    b = 20
    assert a - b == 40


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.skip
def test_function3():
    a = 50
    b = 3
    assert a * b == 150


@pytest.mark.sanity
@pytest.mark.skipif(browser == 'Chrome', reason="can not execute on chrome")
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
