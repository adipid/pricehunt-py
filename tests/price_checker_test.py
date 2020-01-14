import unittest

import price_checker


class PriceCheckerTest(unittest.TestCase):
    def test_get_lowest_price(self):
        price = price_checker.get_lowest_price("https://prisguiden.no/produkt/logitech-mx-master-3-399986")
        self.assertEqual("999", price)

    def test_compare_prices(self):
        price = price_checker.compare_prices("https://prisguiden.no/produkt/logitech-mx-master-3-399986", "1199")
        self.assertEqual("Logitech MX Master 3, 200", price)


if __name__ == '__main__':
    unittest.main()
