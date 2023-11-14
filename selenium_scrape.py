from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

sort_params = {"lowest_comparison_price": "&sort=comparisonPrice%3Aasc",
                     "highest_comparison_price": "&sort=comparisonPrice%3Adesc" }

# Init driver
def init_driver() -> webdriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_searches(query: str, output_json: bool, print_results=False, sorting_parameters="") -> dict:
    """Query the S-Kaupat database

    query: str, the query string

    output_json: bool, if False, prints query results, if True, outputs to queryResults.json

    print_results: bool, if True, prints results to console

    sorting_parameters: "lowest_comparison_price", "highest_comparison_price" or leave blank for no sorting

    """
    driver = init_driver()
    url = "https://www.s-kaupat.fi/hakutulokset?queryString="
    if sorting_parameters != "":
        driver.get(url + query + sort_params[sorting_parameters])
    else:
        driver.get(url + query)
    element = WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "article[data-test-id=product-card]"))
   )
    soup = BeautifulSoup(driver.page_source, "html.parser")
    products_json = query_to_json(soup)
    if output_json:
       with open("queryResults.json", "w") as file:
           json.dump(products_json, file, indent=4)

    if print_results:
        print(products_json)
    driver.quit()

    return products_json


def query_to_json(soup: BeautifulSoup) -> dict:
    products = {}
    for index, tag in enumerate(soup.select("article[data-test-id=product-card]", limit=5)):
        products.update({index: {}})
        products[index].update({"product_name": tag.select_one("a[data-test-id=product-card__productName]").text})
        products[index].update({"Unit price": tag.select_one("span[data-test-id=product-price__unitPrice]").text})
        products[index].update({"Comparison price": tag.select_one("div[data-test-id=product-card__productPrice__comparisonPrice]").text})

    return products
