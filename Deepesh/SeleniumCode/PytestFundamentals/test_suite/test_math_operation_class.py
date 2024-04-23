class TestMathOperation:
    def test_addition(self):
        num1 = 40
        num2 = 60
        assert num1 + num2 == 100

    def test_multiplication(self):
        num1 = 4
        num2 = 6
        assert num1 * num2 == 25

    def test_division(self):
        num1 = 14
        num2 = 2
        assert num1 // num2 == 7
