import requests
from bs4 import BeautifulSoup


class Product:
    def __init__(self, data):
        url = data["url"]
        self.purchased_price = data["purchase_price"]
        self.purchased_date = data["purchase_price"]
        self.shop = data["shop"]

        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")

        self.name = self.soup.find('h1', attrs={'class': 'product-title'}).text.strip()
        self.price = self.soup.find_all('div', attrs={'class': 'product-price'})[0]["data-price"]

