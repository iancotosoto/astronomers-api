import json

from app.config.config import Config
from app.models.astronomer import Astronomer
import app.data.utils.requester as requester
import app.data.utils.converter as converter
import app.data.utils.files_managment as files_managment

# Functions
# Function to get all countries from the website
def get_astronomers():
    """
    Get all astronomers (used to generate the countries.json 
                       and countries.html in data/files/countries)
    """
    astronomers = []
    soup = requester.get_soup(Config.ASTRONOMERS_SOURCE) # The result is in files/countries
    soup_filtered = soup.find("table", class_="wikitable sortable") # Get the first table (astronomers info)
    for astronomer_row in soup_filtered.find_all("tr")[1:]: # Get all rows

        astronomer_info = astronomer_row.find_all("td") # Get all columns
        # Get the data
        name = astronomer_info[0].text
        countries = astronomer_info[1].text.split("/")
        birth_year = converter.convert_year(astronomer_info[2].text) if len(astronomer_info) >= 3 else -1
        death_year = converter.convert_year(astronomer_info[3].text) if len(astronomer_info) == 4 else -1

        # Create and append the astronomer (id is 0 because it will be set in the db)
        astronomer = Astronomer(0, name, birth_year, death_year, countries) # Create a country object
        astronomers.append(astronomer.to_dict_no_id())
    data = {"astronomers": astronomers}

    # Generate the files
    files_managment.generate_file("./data_files/json/astronomers", ".json", json.dumps(data, indent=5, ensure_ascii=False)) # Generate the countries.html file
    # Add more types of files if needed

    return astronomers