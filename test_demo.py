import pytest


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b", [
    (3, 5), (-1, -2)
], ids=["int", "minus"])
def test_add(a, b):
    assert add_function(a, b) == a + b
