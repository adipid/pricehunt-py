import os
import sys
import json
from product import Product

json_filename = "products.json"
cwd = os.path.dirname(os.path.realpath(__file__))
products_data = {}
products_list = []


def load_json(path):
    with open(path) as json_file:
        imported_file = json.load(json_file)
        return imported_file


def check_if_data_exists():
    if not os.path.isfile(json_filename):
        file = open(json_filename, "w")
        file.write("[]")
        file.close()


def main():
    check_if_data_exists()
    global products_data
    products_data = load_json(r"" + cwd + "/" + json_filename)
    product_init()
    menu()


def product_init():
    for i in range(len(products_data)):
        products_list.append(Product(products_data[i]))


def menu():
    print("************MAIN MENU**************\n"
          "Please enter a number\n"
          "1: Add new product(s) to the list\n"
          "2: Remove product(s) from the list\n"
          "3: See details from the list\n"
          "4: Run checker\n"
          "5: Quit\n\n")
    while True:
        choice = input("Please enter your choice: ")
        if choice not in menu_options:
            print("Please select from the menu above")
            continue
        break

    menu_options[choice]()


def return_to_menu():
    want_to_return = input("Return to main menu? Yes/No\n")
    if want_to_return == "Yes".lower() or want_to_return == "y".lower():
        print("\nReturning to main menu\n")
        menu()
    else:
        print("Exiting...")
        menu_options["q"]()


def add_product():
    """
    Add product(s) to the product-list and updates json-data
    """

    # Need URL, date, price and shop
    url = input("Please enter prisguiden.no URL:\n").replace(" ", "")
    date = input("Please enter purchase date: (2020-12-24)\n")
    price = input("Please enter the purchase price: (without spaces)\n")
    shop = input("Please enter the store/shop name:\n")

    new_product = {
        "url": url,
        "purchase_date": date,
        "purchase_price": price,
        "shop": shop
    }

    # Adds the product to the existing list
    products_list.append(Product(new_product))

    # Adds the product to the  data
    products_data.append(new_product)

    # Updates with the new product
    with open(json_filename, "w") as json_file:
        json.dump(products_data, json_file, indent=2)

    return_to_menu()


def remove_product():
    """
    Removes product(s) from the product-list
    and updates json-data
    """

    remove_index = int(input("Which product do you want to remove? ")) - 1

    # Removes the product from existing list
    products_list.pop(int(remove_index))

    # Removes the product from the json-file data
    products_data.pop(int(remove_index))

    # Updates json-file with the removed product
    with open(json_filename, "w") as json_file:
        json.dump(products_data, json_file, indent=2)

    return_to_menu()


def detailed_list():
    index = 1
    for product in products_list:
        print(str(index) + "\t" + "Name: " + product.name +
              "\n\t" + "Purchase price: " + product.purchased_price +
              "\n\t" + "Lowest price: " + product.price +
              "\n\t" + "Price difference: " + product.price_difference +
              "\n\t" + "Purchase date: " + str(product.purchased_date) +
              "\n\t" + "Days since purchase: " + str(product.days_since_purchase) +
              "\n\t" + "Can you use open policy: " + str(product.open_policy) + "\n")
        index += 1

    return_to_menu()


def run_checker():
    os.system("python3 checker.py")
    return_to_menu()


menu_options = {
    "1": add_product,
    "2": remove_product,
    "3": detailed_list,
    "4": run_checker,
    "5": sys.exit,
    "q": sys.exit
}

if __name__ == '__main__':
    main()
