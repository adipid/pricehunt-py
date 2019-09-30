import price_checker
import json


def main():
    products = load_json("products.json")
    #price = price_checker.get_lowest_price("https://prisguiden.no/produkt/logitech-mx-master-3-399986")
    #print(price)

    for i in range(len(products["products"])):
        url = products["products"][i]["url"]
        purchase_price = products["products"][i]["purchase_price"]
        #test = price_checker.check_price(url)
        print(price_checker.compare_prices(url, purchase_price))


def load_json(filename):
    with open(filename) as json_file:
        imported_file = json.load(json_file)
        return imported_file


if __name__ == '__main__':
    main()
