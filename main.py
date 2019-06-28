import requests
from bs4 import BeautifulSoup

r = requests.get("https://yellowpages.com.tr/ara?q=ankara+cafe")
soup = BeautifulSoup(r.content)
