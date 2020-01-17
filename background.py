import json
import pync
import time
import daemon

import main


main.product_init()

with daemon.DaemonContext():
    while True:
        pync.notify("Started the background script!", title="Pricehunt-py")

        for product in main.products_list:
            if int(product.last_check_price) == int(product.price_difference):
                break

            if int(product.purchased_price) > int(product.price):
                pync.notify(product.name + " price has changed!", title="Pricehunt-py", open=product.url)
                product.last_check_price = int(product.price_difference)

        # Checks again every hour
        time.sleep(3600)
