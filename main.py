import price_checker
import json


def main():
    products_data = load_json("products.json")

    # Compare prices
    for i in range(len(products_data["products"])):
        url = products_data["products"][i]["url"]
        purchase_price = products_data["products"][i]["purchase_price"]
        print(price_checker.compare_prices(url, purchase_price))


def load_json(filename):
    with open(filename) as json_file:
        imported_file = json.load(json_file)
        return imported_file


if __name__ == '__main__':
    main()
