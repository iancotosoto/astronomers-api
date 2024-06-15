import json

from app.data.utils.files_managment import read_file

# Functions
# Get countries
def get_countries():
    countries = read_file("./data_files/json/countries", ".json")
    countries = json.loads(countries)
    countries = countries["countries"]
    return countries

# Get countries names
def get_countries_names():
    countries = get_countries()
    countries_names = [country["name"] for country in countries]
    return countries_names