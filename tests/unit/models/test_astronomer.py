import pytest
from app.models.astronomer import Astronomer

@pytest.fixture
def astronomer():
    return Astronomer(id=1, name='Galileo Galilei', birth_year=1564, death_year=1642, countries=['Italy'])

def test_getters(astronomer):
    assert astronomer.get_id() == 1
    assert astronomer.get_name() == 'Galileo Galilei'
    assert astronomer.get_birth_year() == 1564
    assert astronomer.get_death_year() == 1642
    assert astronomer.get_countries() == ['Italy']

def test_setters(astronomer):
    astronomer.set_id(2)
    astronomer.set_name('Isaac Newton')
    astronomer.set_birth_year(1643)
    astronomer.set_death_year(1727)
    astronomer.set_countries(['United Kingdom'])
    
    assert astronomer.get_id() == 2
    assert astronomer.get_name() == 'Isaac Newton'
    assert astronomer.get_birth_year() == 1643
    assert astronomer.get_death_year() == 1727
    assert astronomer.get_countries() == ['United Kingdom']

def test_to_dict(astronomer):
    expected_dict = {
        "id": 1,
        "name": 'Galileo Galilei',
        "birth_year": 1564,
        "death_year": 1642,
        "countries": ['Italy']
    }
    assert astronomer.to_dict() == expected_dict

def test_to_dict_no_id(astronomer):
    expected_dict_no_id = {
        "name": 'Galileo Galilei',
        "birth_year": 1564,
        "death_year": 1642,
        "countries": ['Italy']
    }
    assert astronomer.to_dict_no_id() == expected_dict_no_id