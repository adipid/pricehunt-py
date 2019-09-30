import price_checker


def main():
    price = price_checker.get_lowest_price("https://prisguiden.no/produkt/logitech-mx-master-3-399986")
    print(price)


if __name__ == '__main__':
    main()
