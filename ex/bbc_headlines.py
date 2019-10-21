from bs4 import BeautifulSoup
import requests

bbc_home = requests.get("https://www.bbc.com")
bs = BeautifulSoup(bbc_home.text, 'html.parser')

for t in bs.find_all("h3", class_='media__title'):
    print(t.text.strip(" "))
