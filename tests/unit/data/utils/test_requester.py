import pytest
import requests
import requests_mock
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

from app.data.utils.requester import get_html, get_soup

# get_html
def test_get_html_success(requests_mock):
    url = "http://example.com"
    expected_html = "<html><body><h1>Example Domain</h1></body></html>"
    requests_mock.get(url, text=expected_html)
    
    html = get_html(url)
    assert html == expected_html

def test_get_html_failure(requests_mock):
    url = "http://example.com"
    requests_mock.get(url, status_code=404)
    
    with pytest.raises(RequestException):
        get_html(url)

# get_soup
def test_get_soup_success(requests_mock):
    url = "http://example.com"
    expected_html = "<html><body><h1>Example Domain</h1></body></html>"
    requests_mock.get(url, text=expected_html)
    
    soup = get_soup(url)
    assert isinstance(soup, BeautifulSoup)
    assert soup.h1.text == "Example Domain"

def test_get_soup_failure(requests_mock):
    url = "http://example.com"
    requests_mock.get(url, status_code=404)
    
    with pytest.raises(RequestException):
        get_soup(url)