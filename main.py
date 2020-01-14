import price_checker
import json

from product import Product


def main():
    products_data = load_json("products.json")

    products_list = []

    for i in range(len(products_data["products"])):
        products_list.append(Product(products_data["products"][i]))

    # Compare prices
    for i in range(len(products_list)):
        print(products_list[i].name + ", " +
              price_checker.compare_prices(products_list[i].price, products_list[i].purchased_price))


def load_json(filename):
    with open(filename) as json_file:
        imported_file = json.load(json_file)
        return imported_file


if __name__ == '__main__':
    main()
