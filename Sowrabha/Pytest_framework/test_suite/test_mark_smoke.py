import pytest

# @pytest.mark.smoke
# def test_add():
#     a=10
#     b=20
#     assert a+b==35
#
# @pytest.mark.sanity
# def test_sub():
#     a=40
#     b=30
#     assert a_b==10
#
# @pytest.mark.smoke
# def test_mul():
#     a=50
#     b=5
#     assert a*b==250
#
# @pytest.mark.regression
# def test_div():
#     a=60
#     b=2
#     assert a/b==30
#
# @pytest.mark.smoke
# def test_power():
#     a=60
#     b=10
#     c=20
#     assert a+b+c==90
#Above code is to execute only smoke cases[for my understanding]
#way to execcute Open terminal then [ python -m pytest -v -m smoke .\ test_mark_smoke.py   ]
@pytest.mark.smoke
def test_add():
    a=10
    b=20
    assert a+b==35

@pytest.mark.sanity
def test_sub():
    a=40
    b=30
    assert a-b==10

@pytest.mark.smoke
def test_mul():
    a=50
    b=5
    assert a*b==250

@pytest.mark.regression
def test_div():
    a=60
    b=2
    assert a/b==30

@pytest.mark.smoke
def test_power():
    a=60
    b=10
    c=20
    assert a+b+c==90
