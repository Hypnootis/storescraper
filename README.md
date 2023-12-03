# storescraper
Scraping product prices from the S-Kaupat grocery website

Scraping is done with the 'selenium' and 'BeautifulSoup4 4.12.2' libraries. You'll also need a [webdriver](https://www.selenium.dev/documentation/webdriver/)!

## Steps to test:



Recommended to create a virtual environment for the dependencies, and make sure you have that webdriver installed!

-1. Clone the project and open up your preferred terminal program in the directory

0. If you don't have Python virtual environment installed:

```python3 -m pip install virtualenv```

### 1. Create a virtual environment with:

```python3 -m venv .venv```

### 2. And enter into it with:

```.venv/Scripts/activate```

Or if you're on Unix/MacOS:

```source .venv/bin/activate```

### 3. Install dependencies with:
```cd scraping && pip install -r ./requirements.txt```

### 4. You can then run test.py to test out the scraping!
```python3 test.py```
