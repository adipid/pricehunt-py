import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

import price_checker


class Product:
    def __init__(self, data):
        url = data["url"]
        self.purchased_price = data["purchase_price"]
        self.purchased_date = data["purchase_date"]
        self.purchased_date = datetime.strptime(self.purchased_date, "%Y-%m-%d").date()
        self.shop = data["shop"]

        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")

        self.name = self.soup.find('h1', attrs={'class': 'product-title'}).text.strip()
        self.price = self.soup.find_all('div', attrs={'class': 'product-price'})[0]["data-price"]
        self.price_difference = price_checker.compare_prices(self.price, self.purchased_price)

        today = date.today()

        self.days_since_purchase = str((today - self.purchased_date).days)
        open_policy = price_checker.open_policy(self.days_since_purchase, self.shop)
        if open_policy:
            self.open_policy = "Yes"
        else:
            self.open_policy = "No"
