import app.data.utils.validator as validator

# Functions
# Countries
def convert_continent(continent:str):
    return "America" if continent == "Americas" else continent

# Astronomers
def convert_year(year:str):
    year = year.strip()
    return int(year) if validator.validate_year(year) else -1