import pytest
from pythoncode.calculator import Calculator


class TestCase:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 3), (-1, -2, -3), (10, 20, 30)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 2, 1), (-3, -2, -1), (30, 20, 10)
    ], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 2), (-1, -2, 2), (10, 20, 200)
    ], ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (4, 2, 2), (-4, -2, 2), (40, 20, 2)
    ], ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)


if __name__ == '__main__':
    pytest.main("-sv")
