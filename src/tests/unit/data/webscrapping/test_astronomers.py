import json
import pytest
from bs4 import BeautifulSoup
from unittest.mock import patch, MagicMock

from app.data.webscrapping.astronomers import get_astronomers

@pytest.fixture
def mock_soup():
    mock_soup = BeautifulSoup("<table class='wikitable sortable'><tr><td>Name</td><td>Country</td><td>Birth Year</td><td>Death Year</td></tr><tr><td>Galileo Galilei</td><td>Italy</td><td>1564</td><td>1642</td></tr></table>", "html.parser")
    return mock_soup

@pytest.fixture
def mock_requests_get():
    mock_response = MagicMock()
    mock_response.text = "dummy response"
    return mock_response

@pytest.fixture
def mock_converter():
    mock_convert_year = MagicMock()
    mock_convert_year.return_value = 1564  # Simulate convert_year function
    return mock_convert_year

@pytest.fixture
def mock_generate_file():
    return MagicMock()

@patch('app.data.utils.requester.get_soup')
@patch('app.data.utils.converter.convert_year')
@patch('app.data.utils.files_management.generate_file')
def test_get_astronomers(mock_generate_file, mock_convert_year, mock_get_soup, mock_soup, mock_requests_get):
    mock_get_soup.return_value = mock_soup
    mock_convert_year.side_effect = lambda year: {
        "1564": 1564,
        "1642": 1642
    }[year.strip()] # Simulate convert_year function
    mock_requests_get.return_value = mock_requests_get

    result = get_astronomers()

    assert len(result) == 1
    astronomer = result[0]
    assert astronomer['name'] == "Galileo Galilei"
    assert astronomer['birth_year'] == 1564
    assert astronomer['death_year'] == 1642
    assert astronomer['countries'] == ["Italy"]

    # Check if generate_file was called
    assert mock_generate_file.called

    # Check the arguments of the generate_file call
    call_args = mock_generate_file.call_args
    assert call_args[0][0] == "./data_files/json/astronomers"
    assert call_args[0][1] == ".json"
    generated_data = json.loads(call_args[0][2])
    assert len(generated_data['astronomers']) == 1
    assert generated_data['astronomers'][0]['name'] == "Galileo Galilei"