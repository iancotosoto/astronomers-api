import re

# Functions
# Country
def validate_code_country(code_country: str) -> bool:
    """
    Validate the code of a country (ISO 3166: 3 letters)
    """
    return re.match(r"^[A-Z]{3}$", code_country) != None

# Astronomers
def validate_year(year: str) -> bool:
    """
    Validate the year of birth or death of an astronomer (1 to 4 digits)
    Only after christ and in normal conditions (digits)
    """
    return re.match(r"^\d{1,4}$", year) != None