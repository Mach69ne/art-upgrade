from bs4 import BeautifulSoup
import requests
import json
import mysql.connector
mydb = mysql.connector.connect(
  host="sql497.main-hosting.eu",
  user="u381612044_amtonedevs",
  password="AtSkovlePeng3$$",
  database="u381612044_raid2earn"
)
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
    with open(mint+".json","w") as f:
        json.dump(soup,f)
    f.close()

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM old_apes")

myresult = mycursor.fetchall()
for item in myresult:
        mint = item[1]
        url = item[2]
        if mint=="HbekMP5AhveyzB64A22assnHsL1RSWGEQ98D6hgVQ1cX":
            scraper(url,mint)
