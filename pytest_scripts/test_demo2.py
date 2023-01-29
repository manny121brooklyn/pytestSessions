import pytest

@pytest.mark.login
def test_login():
    assert 'hello' == 'hello'


def test_basic7():
    assert 'mansur' == 'Mansur'