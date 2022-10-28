import pytest


class Test_demo():
    @pytest.mark.demo
    def test_one(self):
        print("第一条用例")

    @pytest.mark.smoke
    def tets_two(self):
        print("第二条用例")

# if __name__ == '__main__':
#     pytest.main("-sv -m")
