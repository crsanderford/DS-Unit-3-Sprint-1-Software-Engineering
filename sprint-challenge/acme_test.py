#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, adj, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5"""
        prod = Product('Slightly Splodey Thing')
        self.assertEqual(prod.flammability, 0.5)

    def test_steal_and_splode(self):
        """Remember when people were freaking out about CERN making a black hole?"""
        experimental_ordnance = Product('False Vacuum Degenerator', price=2E6,
                                        weight=2E3, flammability=9E99)
        self.assertEqual(experimental_ordnance.stealability(),
                         'Very stealable!')
        self.assertEqual(experimental_ordnance.explode(), '...BABOOM!!')
        self.assertEqual(experimental_ordnance.bang_per_buck(), 'Exciting!')


class AcmeReportTests(unittest.TestCase):
    """Testing our tests' testability."""
    def test_default_num_products(self):
        """Check that the default number of generated products is 30."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Ensure that generated products' names are valid."""
        items = generate_products()
        for item in items:
            an_adjective, a_noun = item.name.split(' ')
            self.assertIn(an_adjective, adj)
            self.assertIn(a_noun, noun)


if __name__ == '__main__':
    unittest.main()
