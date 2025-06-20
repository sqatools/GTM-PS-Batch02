import pytest

"""
# scope of the feature 
1). function level : When we set function level scope for the fixture function, then fixture call ifself
                     before and after execution of each test function.
                     e.g @pytest.fixture(scope="function")
                           
2). module level : When we set module level scope for the fixture, then fixture function will only 
                   execute before execution started and end of the execution of all test cases completed.
                  e.g @pytest.fixture(scope="module")
                   
3). session level : If we have multiple test files to execute, then ficture function will initiate before
                   execution of first file, then end of execution of all test files.
                   @pytest.fixture(scope="session")
                   
4). class level :  When we set class level scope then fixture function will execute before execution of
                   test methods and end of execution of all test methods.
                   @pytest.fixture(scope="class")
                   
5). package level : When we set the package level scope, then fixture function will execute before execution
                    initial module of package and after last module of package.

"""


@pytest.fixture(scope="module", autouse=True)
def setup():
    print("----- Test execution started -----")
    yield
    print("\n----- Test execution end ----")


@pytest.mark.smoke
def test_function1():
    a = 50
    b = 60
    assert a + b == 110


@pytest.mark.sanity
def test_function2():
    a = 50
    b = 20
    assert a - b == 40


@pytest.mark.regression
def test_function3():
    a = 50
    b = 3
    assert a * b == 150
