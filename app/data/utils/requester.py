import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# Functions
# Get html as text
def get_html(p_link: str):
    response = requests.get(p_link)
    if response.status_code != 200:
        response.raise_for_status()
    return response.text

# Get BeautifulSoup object
def get_soup(p_link: str):
    response = requests.get(p_link)
    if response.status_code != 200:
        response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup