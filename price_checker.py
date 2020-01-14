# Returns the difference between the purchased price and the lowest price online
def compare_prices(lowest_price, old_price):
    old_price = int(old_price)
    lowest_price = int(lowest_price)

    if old_price > lowest_price:
        difference = old_price - lowest_price
    else:
        difference = lowest_price - old_price

    return str(difference)

