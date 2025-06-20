def test_function1():
    a = 50
    b = 60
    assert a + b == 110


def test_function2():
    a = 50
    b = 20
    assert a - b == 40


def test_function3():
    a = 50
    b = 3
    assert a * b == 150

# python -m pytest -v .\test_smoke_TCs.py
#Command to run pytest code