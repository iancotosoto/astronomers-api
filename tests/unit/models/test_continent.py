import pytest
from app.models.continent import Continent

@pytest.fixture
def continent():
    return Continent(id=1, name='Africa')

def test_getters(continent):
    assert continent.get_id() == 1
    assert continent.get_name() == 'Africa'

def test_setters(continent):
    continent.set_id(2)
    continent.set_name('Asia')
    
    assert continent.get_id() == 2
    assert continent.get_name() == 'Asia'