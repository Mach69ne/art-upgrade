from bs4 import BeautifulSoup
import requests
import json
def scraper(url,mint):
    url = requests.get(url)
    url.status_code
    url.headers
    e = url.content
    soup = BeautifulSoup(e, "html.parser")
    soup = str(soup)
    soup = json.loads(soup)
    number = soup['name'].replace("Forest Apes #","")
    soup["image"] = "https://raw.githubusercontent.com/Sweatyfish/Forestapes-Gen1/main/"+number+".png"
    properties = soup['properties']
    with open(mint+".json","w") as f:
        json.dump(soup,f)
    f.close()


url = "https://arweave.net/-fMZVF026AUBuDilzc7pNt5kBq7-qN5eYdw5hY3ms20"
mint = "3jrGzyQHfRqepKQosFPBJruTnLKNdMf2RzfotQAxMd5o"
scraper(url,mint)
