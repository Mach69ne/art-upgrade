from bs4 import BeautifulSoup
import requests
import json
def scraper(url):
    url = requests.get(url)
    url.status_code
    url.headers
    e = url.content
    soup = BeautifulSoup(e, "html.parser")
    soup = str(soup)
    soup = json.loads(soup)
url = "https://arweave.net/-fMZVF026AUBuDilzc7pNt5kBq7-qN5eYdw5hY3ms20"
scraper(url)
