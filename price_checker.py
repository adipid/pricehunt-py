import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# Returns the lowest price of the product in the URL
def get_lowest_price(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    lowest_price_shop = soup.find_all('div', attrs={'class': 'product-price'})

    price = lowest_price_shop[0]["data-price"]

    return price
