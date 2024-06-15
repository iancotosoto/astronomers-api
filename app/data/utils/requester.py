from bs4 import BeautifulSoup
import requests

# Functions
# Get html as text
def get_html(p_link:str):
    plain_text = requests.get(p_link).text
    return plain_text

# Get BeautifulSoup object
def get_soup(p_link:str):
    plain_text = requests.get(p_link).text
    soup = BeautifulSoup(plain_text, "html.parser")
    return soup
    