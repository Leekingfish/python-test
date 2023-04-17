import pytest
from pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def myfixture():
    # print(f"\n执行我的fixture,里面的参数是:{request.param}\n")
    print("开始计算")
    yield  # 类似return
    print("结束计算")  # 清理数据，关闭数据库链接


def pytest_collection_modifyitems(session, config, items):
    print(type(items))
    items.reverse()  # 顺序翻转
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
