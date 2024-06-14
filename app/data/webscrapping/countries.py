import json

import data.utils.requester as requester
from app.models.country import Country
from app.config import Config

import data.utils.converter as converter
import data.utils.validator as validator
import data.utils.files_managment as files_managment

# Function to get all countries from the website
def get_countries():
    """
    Get all countries (used to generate the countries.json 
                       and countries.html in data/files/countries)
    """
    countries = []
    soup = requester.get_soup(Config.COUNTRIES_SOURCE) # The result is in files/countries
    files_managment.generate_file("./data/files/countries/countries", ".html", soup.prettify()) # Generate the countries.html file
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
    data = {"countries": countries}
    files_managment.generate_file("./data/files/countries/countries", ".json", json.dumps(data, indent=4)) # Generate the countries.html file
    return data