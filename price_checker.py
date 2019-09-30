import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# Returns the lowest price of the product in the URL
def get_lowest_price(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    product_name = soup.find('h1', attrs={'class': 'product-title'})
    lowest_price_shop = soup.find_all('div', attrs={'class': 'product-price'})

    name = product_name.text.strip()
    price = lowest_price_shop[0]["data-price"]

    name_price = name + ", " + price

    return name_price

