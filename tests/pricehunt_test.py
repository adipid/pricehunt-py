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
        for i in range(len(products_data)):
            products_list.append(Product(products_data[i]))

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

    def test_open_policyFalse(self):
        self.assertFalse(price_checker.open_policy(61, "Komplett.no"))

    def test_open_policyTrue0(self):
        self.assertTrue(price_checker.open_policy(60, "Komplett.no"))

    def test_open_policyTrue1(self):
        self.assertTrue(price_checker.open_policy(10, "Komplett.no"))

    def test_add_product(self):
        self.fail()

    def test_remove_product(self):
        self.fail()

    def test_get_list(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()
