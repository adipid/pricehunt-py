import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class Product:
    name = ""

    def __init__(self, url):
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")

        self.name = self.soup.find('h1', attrs={'class': 'product-title'}).text.strip()
        self.price = self.soup.find_all('div', attrs={'class': 'product-price'})[0]["data-price"]


