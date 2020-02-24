import json
import pync
import time

import setup


setup.product_init()

pync.notify("Started the background script!", title="Pricehunt-py")

for product in setup.products_list:
    if int(product.last_check_price) == int(product.price_difference):
        break

    if int(product.purchased_price) > int(product.price):
        pync.notify(product.name + " price has changed!", title="Pricehunt-py", open=product.url)
        product.last_check_price = int(product.price_difference)
