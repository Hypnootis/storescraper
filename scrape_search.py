import requests
from bs4 import BeautifulSoup

url = "https://www.s-kaupat.fi/hakutulokset?queryString="

def get_page(query: str) -> BeautifulSoup:
    page = requests.get(url + query)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup






