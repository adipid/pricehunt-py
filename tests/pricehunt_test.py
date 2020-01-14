import json
import unittest

import price_checker
from product import Product


def load_json(filename):
    with open(filename) as json_file:
        imported_file = json.load(json_file)
        return imported_file


products_data = load_json("test-products.json")
products_list = []


class PricehuntTest(unittest.TestCase):

    def setUp(self):
        for i in range(len(products_data["products"])):
            products_list.append(Product(products_data["products"][i]))

    def test_correct_product0(self):
        self.assertEqual("Logitech MX Master 3", products_list[0].name)

    def test_correct_product1(self):
        self.assertEqual("Logitech MX Keys", products_list[1].name)

    def test_correct_product2(self):
        self.assertEqual("Apple Watch Series 5 Cellular 44mm", products_list[2].name)

    def test_lowest_price_product0(self):
        self.assertEqual("999", products_list[0].price)

    def test_compare_price_product0(self):
        diff = price_checker.compare_prices(products_list[0].price, products_list[0].purchased_price)
        self.assertEqual("200", diff)


if __name__ == '__main__':
    unittest.main()
