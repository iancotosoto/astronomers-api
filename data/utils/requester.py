from bs4 import BeautifulSoup
import requests

def get_html(p_link:str):
    plain_text = requests.get(p_link).text
    return plain_text

def get_soup(p_link:str):
    plain_text = requests.get(p_link).text
    soup = BeautifulSoup(plain_text, "html.parser")
    return soup
    