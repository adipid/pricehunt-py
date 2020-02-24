import json
import pync

import setup

SCRIPT_NAME = "Pricehunt-py"

setup.product_init()
product_data = setup.load_json(r"" + setup.cwd + "/" + "products.json")

pync.notify("Started the background script!", title=SCRIPT_NAME)

for index, product in enumerate(setup.products_list):
    if int(product_data[index]["last_checked_price"]) == int(product.price_difference):
        break

    if int(product.purchased_price) > int(product.price):
        pync.notify(product.name + " price has changed!", title=SCRIPT_NAME, open=product.url)
        product_data[index]["last_checked_price"] = int(product.price_difference)
        with open('products.json', 'w') as f:
            json.dump(product_data, f, indent=2)
