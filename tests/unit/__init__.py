import pytest
from app.models.country import Country

@pytest.fixture
def country():
    return Country(id='USA', name='United States of America', continent='North America')

def test_getters(country):
    assert country.get_id() == 'USA'
    assert country.get_name() == 'United States of America'
    assert country.get_continent() == 'North America'

def test_setters(country):
    country.set_id('CAN')
    country.set_name('Canada')
    country.set_continent('North America')
    
    assert country.get_id() == 'CAN'
    assert country.get_name() == 'Canada'
    assert country.get_continent() == 'North America'

def test_to_dict(country):
    expected_dict = {
        "id": 'USA',
        "name": 'United States of America',
        "continent": 'North America'
    }
    assert country.to_dict() == expected_dict