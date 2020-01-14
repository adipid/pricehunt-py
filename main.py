import sys

import price_checker
import json

from product import Product


def load_json(filename):
    with open(filename) as json_file:
        imported_file = json.load(json_file)
        return imported_file


products_data = load_json("products.json")


def main():
    products_list = []

    for i in range(len(products_data["products"])):
        products_list.append(Product(products_data["products"][i]))

    # Compare prices
    for i in range(len(products_list)):
        print(products_list[i].name + ", " +
              price_checker.compare_prices(products_list[i].price, products_list[i].purchased_price))

    menu()


def menu():
    print("************MAIN MENU**************\n")
    choice = input("1: Add new product(s) to the list\n"
                   "2: Remove product(s) from the list\n"
                   "3: See details from the list\n"
                   "4: Quit\n\n"
                   "Please enter your choice:")
    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        display_list()
    elif choice == "4" or choice.lower() == "q":
        sys.exit()
    else:
        print("You must only select from the menu provided\nPlease try again!")
        menu()


def add_product():
    # Need URL, date, price and shop
    url = input("Please enter prisguiden.no URL:\n").replace(" ", "")
    date = input("Please enter purchase date: (2020-01-01)\n")
    price = input("Please enter the purchase price: (without spaces)\n")
    shop = input("Please enter the store/shop name:\n")

    new_product = {
        "url": url,
        "purchase_date": date,
        "purchase_price": price,
        "shop": shop
    }

    products_data["products"].append(new_product)

    with open("products.json", "w") as json_file:
        json.dump(products_data, json_file, indent=2)


def remove_product():
    # test
    print()


def display_list():
    # test
    print()


if __name__ == '__main__':
    main()
