import pytest
import yaml


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expect",
                         yaml.safe_load(open("./data.yml"))["datas"], yaml.safe_load(open("./data.yml"))["myid"])
def test_add(self, a, b, expect):
    assert expect == add_function(a, b)
