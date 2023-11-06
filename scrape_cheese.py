import requests
from bs4 import BeautifulSoup
"""
    We want a unit price and a per kg cost
"""

url = "https://www.s-kaupat.fi/tuote/valio-hyva-suomalainen-arkir-juusto-e1-25-kg/6408430337590"
url2 = "https://www.s-kaupat.fi/tuote/rainbow-1-kg-kermajuusto/6414893381018"

first_page = requests.get(url)
second_page = requests.get(url2)

first_soup = BeautifulSoup(first_page.content, "html.parser")
second_soup = BeautifulSoup(second_page.content, "html.parser")

def get_unit_price(soup):
    return soup.find("span", attrs={"data-test-id": "product-price__unitPrice"}).text

def get_product_name(soup):
    return soup.find("h1", attrs={"data-test-id": "product-name"}).text

def get_kilo_price(soup):
    return soup.find("div", attrs={"data-test-id": "product-page-price__comparisonPrice"}).text

print(f"Price for {get_product_name(first_soup)}: {get_unit_price(first_soup)} {get_kilo_price(first_soup)}")
print(f"Price for {get_product_name(second_soup)}: {get_unit_price(second_soup)} {get_kilo_price(second_soup)}")