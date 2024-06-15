import pytest

def test_upper():
    assert 'hello'.upper() == 'HELLO'

def test_isupper():
    assert 'HELLO'.isupper()
    assert not 'Hello'.isupper()

def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    with pytest.raises(TypeError):
        s.split(2)