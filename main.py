import price_checker
import json


def main():
    products = load_json("products.json")

    # Compare prices
    for i in range(len(products["products"])):
        url = products["products"][i]["url"]
        purchase_price = products["products"][i]["purchase_price"]
        print(price_checker.compare_prices(url, purchase_price))


def load_json(filename):
    with open(filename) as json_file:
        imported_file = json.load(json_file)
        return imported_file


if __name__ == '__main__':
    main()
