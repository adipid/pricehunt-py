import requests
import urllib.request
import time
from bs4 import BeautifulSoup

soup = ""


# Returns the lowest price of the product in the URL
def get_lowest_price(url):
    soup = get_request(url)

    lowest_price_shop = soup.find_all('div', attrs={'class': 'product-price'})

    name = get_product_name()
    price = lowest_price_shop[0]["data-price"]

    return price


def compare_prices(url, old_price):
    old_price = int(old_price)
    lowest_price = int(get_lowest_price(url))

    if old_price > lowest_price:
        difference = old_price - lowest_price
    else:
        difference = lowest_price - old_price

    return get_product_name() + ", " + str(difference)


def get_request(url):
    response = requests.get(url)
    global soup
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# Cannot be used unless the get_request has been initialized
def get_product_name():
    global soup

    product_name = soup.find('h1', attrs={'class': 'product-title'})
    name = product_name.text.strip()

    return name
