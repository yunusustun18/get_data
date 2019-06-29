import requests
from bs4 import BeautifulSoup

tum_kelimeler = []

url = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

for i in soup.find_all("p"):
    icerik = i.text
    kelimeler = icerik.lower().split()

    for j in kelimeler:
        tum_kelimeler.append(j)
