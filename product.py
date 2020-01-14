import requests
from bs4 import BeautifulSoup


class Product:
    name = ""

    def __init__(self, json):

        url = json["url"]
        self.purchased_price = json["purchase_price"]
        self.purchased_date = json["purchase_price"]
        self.shop = json["shop"]

        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")

        self.name = self.soup.find('h1', attrs={'class': 'product-title'}).text.strip()
        self.price = self.soup.find_all('div', attrs={'class': 'product-price'})[0]["data-price"]

