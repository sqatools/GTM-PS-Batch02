"""
command to install pytest

"""
import pytest
from logging_module import logger


@pytest.mark.smoke
def test_function1():
    a = 50
    b = 60
    logger.info(f"test function1 value a:{a}, b:{b}")
    assert a + b == 110


@pytest.mark.smoke
@pytest.mark.flaky(rerun=2)
def test_function2():
    a = 50
    b = 20
    logger.error(f"test function2 value a:{a}, b:{b}, test failed")
    assert a - b == 40


@pytest.mark.smoke
@pytest.mark.sanity
def test_function3():
    a = 50
    b = 3
    logger.info(f"test function3 value a:{a}, b:{b}")
    assert a * b == 150


@pytest.mark.sanity
def test_function4():
    a = 50
    b = 3
    logger.info(f"test function4 value a:{a}, b:{b}")
    assert a * b == 150


@pytest.mark.regression
def test_function5():
    a = 50
    b = 3
    logger.info(f"test function5 value a:{a}, b:{b}")
    assert a * b == 150


@pytest.mark.regression
def test_function6():
    a = 50
    b = 3
    logger.warning(f"test function6 value a:{a}, b:{b}")
    assert a * b == 150

@pytest.mark.smoke
def test_function7():
    a = 50
    b = 60
    logger.info(f"test function1 value a:{a}, b:{b}")
    assert a + b == 110


@pytest.mark.TEST03
def test_function8():
    a = 50
    b = 20
    logger.error(f"test function2 value a:{a}, b:{b}, test failed")
    assert a - b == 40


@pytest.mark.smoke
@pytest.mark.sanity
def test_function9():
    a = 50
    b = 3
    logger.info(f"test function3 value a:{a}, b:{b}")
    assert a * b == 150


@pytest.mark.sanity
def test_function10():
    a = 50
    b = 3
    logger.info(f"test function4 value a:{a}, b:{b}")
    assert a * b == 150


@pytest.mark.regression
def test_function11():
    a = 50
    b = 3
    logger.info(f"test function5 value a:{a}, b:{b}")
    assert a * b == 150


@pytest.mark.regression
def test_function12():
    a = 50
    b = 3
    logger.warning(f"test function6 value a:{a}, b:{b}")
    assert a * b == 150
