import requests
from bs4 import BeautifulSoup

imdb_url = "https://www.imdb.com/chart/top"

r = requests.get(imdb_url)

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("table", {"class": "chart full-width"})

data = (data[0].contents)[len(data[0].contents) - 2]

data = data.find_all("tr")

for i in data:
    new_data = i.find_all("td", {"class": "titleColumn"})
    veri = new_data[0].text
    veri = veri.replace("\n", "")
    print(veri, "\n-------------\n")
