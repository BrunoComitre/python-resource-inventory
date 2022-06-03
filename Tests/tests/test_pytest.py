# test_pytest
import sys

import pytest


@pytest.mark.example
def test_meu_primeiro_teste() -> None:
    assert 1 == 1

@pytest.mark.example
def test_meu_segundo_teste() -> None:
    assert True

@pytest.mark.example
def test_meu_terceiro_teste() -> None:
    assert 0 == 0

@pytest.mark.example
def test_meu_quarto_teste() -> None:
    assert 1 > 0

@pytest.mark.example
def test_meu_quinto_teste() -> None:
    assert 0 < 1

@pytest.mark.example
def test_meu_sexto_teste() -> None:
    assert 1 != 0

# SKIP

@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    ...

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)

# SKIPIF

@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_function_skip():
    ...

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestPosixCalls:
    def test_function(self):
        "will not be setup or run under 'win32' platform"

# XFAIL

@pytest.mark.xfail
def test_function_fail():
    ...

def valid_config():
    return True

def test_function_fail_two():
    if not valid_config():
        pytest.xfail("failing configuration (but should work)")

@pytest.mark.xfail(reason="known parser issue")
def test_function():
    ...

@pytest.mark.xfail(sys.platform == "win32", reason="does not run on windows")
def test_fail():
    ...

@pytest.mark.xfail
def test_hello():
    assert 0

# USEFIXTURE

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket

# PARAMETRIZE

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
