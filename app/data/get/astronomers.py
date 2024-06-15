import json

from app.data.utils.files_managment import read_file

# Functions
# Get astronomers
def get_astronomers():
    astronomers = read_file("./data_files/json/astronomers", ".json")
    astronomers = json.loads(astronomers)
    astronomers = astronomers["astronomers"]
    return astronomers