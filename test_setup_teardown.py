import pytest


class TestCase():

    def setup_class(self):
        print("类前置")

    def teardown_class(self):
        print("类后置")

    def setup(self):
        print("用例前置")

    def teardown(self):
        print("用例后置")

    def test_login(self):
        print("登录")
