from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Init driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

def get_searches(query: str, driver: webdriver):
   driver.get("https://www.s-kaupat.fi/hakutulokset?queryString=" + query)
   element = WebDriverWait(driver=driver, timeout=5).until(
       EC.visibility_of_element_located((By.CSS_SELECTOR, "article[data-test-id=product-card]"))
   )

get_searches("kana", driver)

soup = BeautifulSoup(driver.page_source, "html.parser")
beautiful_page = soup.prettify()
with open("selenium_cheeses.html", "w") as file:
    file.write(beautiful_page)
driver.quit()