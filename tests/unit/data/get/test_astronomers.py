from unittest.mock import patch, mock_open

from app.data.get.astronomers import get_astronomers

@patch('builtins.open', new_callable=mock_open, read_data='{"astronomers": \
                                                            [{"name": "Marc Aaronson", \
                                                            "birth_year": 1950, \
                                                            "death_year": 1990, \
                                                            "countries": ["United States"]}]}')
def test_get_astronomers(mock_file):
    # Call the function
    astronomers = get_astronomers()

    # Expected data
    expected_astronomers = [
        {
            "name": "Marc Aaronson",
            "birth_year": 1950,
            "death_year": 1990,
            "countries": ["United States"]
        }
    ]
    
    # Assertions
    assert astronomers == expected_astronomers