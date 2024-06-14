import json

import data.utils.requester as requester
from app.models.astronomer import Astronomer
from app.config import Config

import data.utils.converter as converter
import data.utils.validator as validator
import data.utils.files_managment as files_managment

# Function to get all countries from the website
def get_astronomers():
    """
    Get all astronomers (used to generate the countries.json 
                       and countries.html in data/files/countries)
    """
    countries = []
    soup = requester.get_soup(Config.ASTRONOMERS_SOURCE) # The result is in files/countries
    return soup