import data.utils.requester as requester
from app.models.country import Country
from config import Config

import data.utils.converter as converter
import data.utils.validator as validator
from data.utils.files_generator import generate_file

# Function to get all countries from the website
def get_countries():
    """
    Get all countries
    """
    countries = []
    soup = requester.get_soup(Config.COUNTRIES_SOURCE) # The result is in files/countries
    soup = soup.find_all("table", class_="outlinetable")[0] # Get the first table
    for country_info in soup.find_all("tr")[1:]: # Get all rows except the first one
        country_info = country_info.find_all("td") # Get all columns
        country_code = country_info[6].text
        if not validator.validate_code_country(country_code):
            continue
        continent = converter.convert_continent(country_info[0].text)
        country_name = country_info[2].text
        country = Country(country_code, country_name, continent) # Create a country object
        countries.append(country.to_dict())
    return countries