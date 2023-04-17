import pytest, yaml
from pythoncode.calculator import Calculator


def get_data():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["datas1"]
        sub_datas = datas["datas2"]
        mul_datas = datas["datas3"]
        div_datas = datas["datas4"]
        ids = datas["myid"]
        return add_datas, sub_datas, mul_datas, div_datas, ids

class TestCase:
    # def setup_class(self):
    #     self.calc = Calculator()
    #     print("开始计算")
    #
    # def teardown_class(self):
    #     print("结束计算")

    @pytest.mark.parametrize("a,b,expect",
                             get_data()[0],
                             ids=get_data()[4])
    def test_add(self, a, b, expect, myfixture):
        self.calc = Calculator()
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_data()[1],
                             ids=get_data()[4])
    def test_sub(self, a, b, expect):
        self.calc = Calculator()
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_data()[2],
                             ids=get_data()[4])
    def test_mul(self, a, b, expect):
        self.calc = Calculator()
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             get_data()[3],
                             ids=get_data()[4])
    def test_div(self, a, b, expect):
        self.calc = Calculator()
        assert expect == self.calc.div(a, b)

# if __name__ == '__main__':
#     pytest.main("-sv")
