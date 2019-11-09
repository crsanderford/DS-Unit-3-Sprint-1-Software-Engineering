#!/usr/bin/env python

"""Acme inventory management; as random and flammable as our products."""

from random import randint, uniform
from acme import Product

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
# why is 'Rocket' not in this list? Come on.


def generate_products(n_products=30):
    """Randomly generate some Acme products. Default 30."""
    products = []
    for ii in range(n_products):
        name = adj[randint(0, len(adj)-1)] + ' ' + noun[randint(0, len(noun)-1)]
        # ^ couldn't get this line below 80 without getting rid of good whitespace ^
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight,
                        flammability=flammability))
    return products


def inventory_report(products):
    """Aggregate statistics for a list of products."""
    all_names = []
    all_prices = []
    all_weights = []
    all_flammabilities = []
    for product in products:
        all_names.append(product.name)
        all_prices.append(product.price)
        all_weights.append(product.weight)
        all_flammabilities.append(product.flammability)
    print("Acme, Inc. Inventory Report")
    print(f"Unique product names: {len(set(all_names))}")
    print(f"Average price: {sum(all_prices)/len(all_prices)}")
    print(f"Average weight: {sum(all_weights)/len(all_weights)}")
    print("Don't let our liability insurance provider see the next line...")
    print(f"Average flammability: {sum(all_flammabilities)/len(all_flammabilities)}")
    # ^ could rename variable to shorten the line but that reduces legibility ^


if __name__ == '__main__':
    inventory_report(generate_products())
