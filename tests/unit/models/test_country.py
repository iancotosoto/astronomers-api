import pytest
from app.models.country import Country

@pytest.fixture
def country():
    return Country(id='USA', name='United States', continent='America')

def test_getters(country):
    assert country.get_id() == 'USA'
    assert country.get_name() == 'United States'
    assert country.get_continent() == 'America'

def test_setters(country):
    country.set_id('CAN')
    country.set_name('Canada')
    country.set_continent('America')
    
    assert country.get_id() == 'CAN'
    assert country.get_name() == 'Canada'
    assert country.get_continent() == 'America'

def test_to_dict(country):
    expected_dict = {
        "id": 'USA',
        "name": 'United States',
        "continent": 'America'
    }
    assert country.to_dict() == expected_dict