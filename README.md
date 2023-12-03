# storescraper
Scraping product prices from grocery stores and giving tips

Scraping is done with the 'selenium' and 'BeautifulSoup4 4.12.2' libraries. You'll also need a [webdriver](https://www.selenium.dev/documentation/webdriver/)!

Recommended to create a virtual environment for the dependencies.

If you don't have Python virtual environment installed

```python3 -m pip install virtualenv```

Create a virtual environment with

```python3 -m venv .venv```

And enter into it with

```.venv/Scripts/activate```

Or if you're on Unix/MacOS

```source .venv/bin/activate```

Install dependencies with 
```cd scraping && pip install -r ./requirements.txt```

You can then run test.py to test out the scraping.
