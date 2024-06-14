import re

def validate_code_country(code_country: str) -> bool:
    """
    Validate the code of a country
    """
    return re.match(r"^[A-Z]{3}$", code_country) != None