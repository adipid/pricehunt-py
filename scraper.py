import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#
url = "https://prisguiden.no/produkt/logitech-mx-master-3-399986"
response = requests.get(url)

# Checking if the request went through
print(response)

soup = BeautifulSoup(response.text, "html.parser")

lowest_price_shop = soup.find_all('div', attrs={'class': 'product-price'})

price = lowest_price_shop[0]["data-price"]

print(price)
