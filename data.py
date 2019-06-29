import requests
from bs4 import BeautifulSoup


def temizle(kelimeler):
    semboller = "!'^+%&/()=?_>£#$½¾{[]}\|<>|@€.,:;`˙"
    new_kelimeler = []
    for kelime in kelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol, "")
        if (len(kelime) > 0):
            new_kelimeler.append(kelime)
    return new_kelimeler


tum_kelimeler = []

url = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

for i in soup.find_all("p"):
    icerik = i.text
    kelimeler = icerik.lower().split()

    for j in kelimeler:
        tum_kelimeler.append(j)

tum_kelimeler = temizle(tum_kelimeler)
for i in tum_kelimeler:
    print(i)
