import pytest

def test_login():
    assert True

@pytest.mark.login
def test_basic4():
    assert False
