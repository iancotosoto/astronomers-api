import json
import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from app.data.webscrapping.countries import get_countries

@pytest.fixture
def mock_soup():
    mock_soup = BeautifulSoup("<html>\
            <body>\
                <table class='outlinetable'>\
                    <tr><td>Americas</td><td>--</td><td>United States</td><td>...</td><td>...</td><td>...</td><td>USA</td></tr>\
                    <tr><td>Europe</td><td>...</td><td>Spain</td><td>...</td><td>...</td><td>...</td><td>ESP</td></tr>\
                </table>\
            </body>\
        </html>", "html.parser")
    return mock_soup

@pytest.fixture
def mock_requests_get():
    mock_response = MagicMock()
    mock_response.text = "dummy response"
    return mock_response

@pytest.fixture
def mock_validator():
    mock_validate_code_country = MagicMock()
    mock_validate_code_country.side_effect = lambda code: code != "--"
    return mock_validate_code_country

@pytest.fixture
def mock_converter():
    mock_convert_continent = MagicMock()
    mock_convert_continent.side_effect = lambda continent: "America" if continent == "Americas" else continent
    return mock_convert_continent

@pytest.fixture
def mock_generate_file():
    return MagicMock()

@patch('app.data.utils.requester.get_soup')
@patch('app.data.utils.validator.validate_code_country')
@patch('app.data.utils.converter.convert_continent')
@patch('app.data.utils.files_managment.generate_file')
def test_get_countries(mock_generate_file, mock_convert_continent, mock_validate_code_country, mock_get_soup, mock_soup, mock_requests_get):
    mock_get_soup.return_value = mock_soup
    mock_validate_code_country.side_effect = lambda code: code != "--"
    mock_convert_continent.side_effect = lambda continent: "America" if continent == "Americas" else continent
    mock_requests_get.return_value = mock_requests_get

    result = get_countries()

    assert 'countries' in result
    countries = result['countries']
    assert len(countries) == 1

    # Check the first country
    country = countries[0]
    assert country['id'] == "ESP"
    assert country['name'] == "Spain"
    assert country['continent'] == "Europe"

    # Check if generate_file was called
    assert mock_generate_file.called

    # Check the arguments of the generate_file call
    call_args = mock_generate_file.call_args
    assert call_args[0][0] == "./data_files/json/countries"
    assert call_args[0][1] == ".json"
    generated_data = json.loads(call_args[0][2])
    assert len(generated_data['countries']) == 1
    assert generated_data['countries'][0]['id'] == "ESP"