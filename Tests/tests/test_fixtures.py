from faker import Faker
from pytest import fixture, mark


@fixture
def my_fixture():
    """ This text will appear when you execute the command: pytest --fixtures """
    return "Hello"

# TEMPDIR - Temporary Directory

# CAPTURE - Capturing Output

# CAPLOG - Capturing Logs

# MONKEYPATCH - Monkeypatching

# MOCK - Mocking
