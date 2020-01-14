import price_checker
import json

from product import Product


def main():
    products_data = load_json("products.json")

    products_list = []
    for i in range(len(products_data["products"])):
        products_list.append(Product(products_data["products"][i]["url"]))

    print(products_list[0].name)

    # Compare prices
    #for i in range(len(products_data["products"])):
     #   url = products_data["products"][i]["url"]
      #  purchase_price = products_data["products"][i]["purchase_price"]
       # print(price_checker.compare_prices(url, purchase_price))


def load_json(filename):
    with open(filename) as json_file:
        imported_file = json.load(json_file)
        return imported_file


if __name__ == '__main__':
    main()
