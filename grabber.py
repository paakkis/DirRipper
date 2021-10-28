import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def grabber(dirs, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href$='.pdf']"):
        filename = os.path.join(dirs, link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link['href'])).content)