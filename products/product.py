
def create_product(name, price):
    return {
        "name": name,
        "price": price
    }


def print_product(product):
    print("Product:", product["name"])
    print("Price:", product["price"])

    