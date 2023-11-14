from selenium_scrape import get_searches

results = get_searches("maito", True, False)

print(results[0])

# You can also use the default values:
# get_searches("juusto", True)