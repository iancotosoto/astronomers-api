from app.data.utils.converter import convert_continent, convert_year

# Continent conversion
def test_convert_americas():
    assert convert_continent("Americas") == "America"

def test_convert_other():
    assert convert_continent("Europe") == "Europe"
    assert convert_continent("Asia") == "Asia"
    assert convert_continent("Africa") == "Africa"
    assert convert_continent("Oceania") == "Oceania"
    assert convert_continent("Antarctica") == "Antarctica"

# Year conversion
def test_convert_year():
    assert convert_year("2024") == 2024
    assert convert_year("abcd") == -1
    assert convert_year("12345") == -1
    assert convert_year("0") == 0
    assert convert_year("9999") == 9999
    assert convert_year("10000") == -1