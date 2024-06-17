from unittest.mock import patch, mock_open

from app.data.get.countries import get_countries, get_countries_names

@patch('builtins.open', new_callable=mock_open, read_data='{"countries": \
                                                            [{"id": "GBR", \
                                                             "name": "United Kingdom", \
                                                             "continent": "Europe"}]}')
def test_get_countries(mock_file):
    # Call the function
    astronomers = get_countries()

    # Expected data
    expected_countries = [{"id": "GBR", "name": "United Kingdom", "continent": "Europe"}]

    # Assertions
    assert astronomers == expected_countries

@patch('app.data.get.countries.get_countries')
def test_get_countries_names(mock_get_countries):
    # Mock para get_countries
    mock_get_countries.return_value = [
        {"id": "GBR", "name": "United Kingdom", "continent": "Europe"},
        {"id": "FRA", "name": "France", "continent": "Europe"}
    ]

    # Call the function
    result = get_countries_names()

    # Expected data
    expected_data = ["United Kingdom", "France"]
    
    # Assertions
    assert result == expected_data
    mock_get_countries.assert_called_once()