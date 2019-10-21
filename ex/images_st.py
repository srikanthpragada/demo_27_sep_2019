from bs4 import BeautifulSoup
import requests

st_home = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(st_home.text, 'html.parser')

for t in bs.find_all("img"):
    if 'title' in t.attrs:
        title = t['title']
    else:
        title = ""

    print(f"{t['src']} - {title}")
