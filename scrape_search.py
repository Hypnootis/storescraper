from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://www.s-kaupat.fi/hakutulokset?queryString="

def get_page(query: str) -> BeautifulSoup:
    s = HTMLSession()
    page = s.get(url + query)
    page.html.render()
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

with open("cheeses.html", "w") as file:
    file.write(get_page("arkijuusto").text)
"""
products = get_page("arkijuusto").findAll("div", attrs={"role": "listitem"})

for product in products:
    print(product)
"""


