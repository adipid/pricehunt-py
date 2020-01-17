import json
import os

# Directory of the script
cwd = os.path.dirname(os.path.realpath(__file__))
with open(r"" + cwd + "/store-policy.json") as json_file:
    store_policy = json.load(json_file)


# Returns the difference between the purchased price and the lowest price online
def compare_prices(lowest_price, old_price):
    old_price = int(old_price)
    lowest_price = int(lowest_price)

    if old_price > lowest_price:
        difference = old_price - lowest_price
    else:
        difference = lowest_price - old_price

    return str(difference)


def open_policy(days_since_purchase, store):
    days_since_purchase = int(days_since_purchase)

    for i in range(len(store_policy)):
        if store_policy[i]["name"] == store:
            if store_policy[i]["policy"] >= days_since_purchase:
                return True
    return False
