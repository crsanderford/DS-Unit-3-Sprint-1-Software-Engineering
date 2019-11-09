#!/usr/bin/env python

"""Class to represent acme products."""

from random import randint


class Product:
    """No-frills acme product class. A bit steal-y, a bit splode-y."""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        # set the initial values for a product.
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """Produce product's pilfering potential."""
        price_per_pound = (self.price / self. weight)
        if price_per_pound < 0.5:
            return 'Not so stealable...'
        elif ((price_per_pound >= 0.5) and (price_per_pound < 1.0)):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """Interpret item's ignition inclination."""
        megaton_yield = (self.flammability * self.weight)
        if megaton_yield < 10.0:
            return '...fizzle.'
        elif ((megaton_yield >= 10.0) and (megaton_yield < 50.0)):
            return '...boom!'
        else:
            return '...BABOOM!!'

    def bang_per_buck(self):
        """A coyote is an economical creature."""
        megaton_yield = (self.flammability * self.weight)
        damage_per_dollar = (megaton_yield / self.price)
        if damage_per_dollar < 1.0:
            return 'Disappointing.'
        elif ((damage_per_dollar >= 1.0) and (damage_per_dollar < 5.0)):
            return 'Middling.'
        else:
            return 'Exciting!'


class BoxingGlove(Product):
    """I love the Power Glove. It's so bad."""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        """Give 'em a good drubbing, will you?"""
        if self.weight < 5.0:
            return 'That tickles.'
        elif ((self.weight >= 5.0) and (self.weight < 15.0)):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'

    def explain_the_docstring(self):
        return 'https://www.youtube.com/watch?v=KZErvASwdlU'
