from app.data.utils.validator import validate_code_country, validate_year

# Validate country code
def test_validate_code_country():
    # True cases
    assert validate_code_country("ESP") is True
    assert validate_code_country("GBR") is True
    assert validate_code_country("CRC") is True

    # False cases
    assert validate_code_country("ESPS") is False
    assert validate_code_country("ES") is False
    assert validate_code_country("esp") is False

# Year validator
def test_validate_year():
    # True cases
    assert validate_year("2024") is True
    assert validate_year("0") is True
    assert validate_year("9999") is True
    
    # False cases
    assert validate_year("abcd") is False
    assert validate_year("12345") is False
    assert validate_year("10000") is False