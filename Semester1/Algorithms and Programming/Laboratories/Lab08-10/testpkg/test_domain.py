#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
MyVectorTest class
"""


import unittest
from domain.business import MyVector


class MyVectorTest(unittest.TestCase):
    """
    MyVector test class. It uses unittest.TestCase
    """

    def setUp(self):
        """
        lets make a setup
        """
        self.vector = MyVector(name="Raul", color="r", _type=1, values=[1, 2, 3])
        self.second_vector = MyVector(name="Alex", color="b", _type=2, values=[4, 5, 6])

    def test_attributes(self):
        """
        testing attributes
        """
        self.assertTrue(self.vector.name == "Raul")
        self.assertTrue(self.vector.color == "r")
        self.assertTrue(self.vector.type == 1)
        self.assertTrue(all([x in self.vector.values for x in [1, 2, 3]]))
        self.assertTrue(len(self.vector.values) == 3)

    def test_operators(self):
        """
        testing operators like __add__ __sub__ __mul__
        """
        self.vector + 1
        self.assertTrue(all([x in self.vector.values for x in [2, 3, 4]]))
        self.assertTrue(len(self.vector.values) == 3)

        self.vector - 1
        self.assertTrue(all([x in self.vector.values for x in [1, 2, 3]]))
        self.assertEqual(len(self.vector.values), 3)

        self.vector * 2
        self.assertEqual(list(self.vector.values), [2, 4, 6])
        self.assertEqual(self.vector * self.second_vector, 64)

    def test_methods(self):
        """
        testing methods
        """
        self.assertEqual(self.vector.get_sum(), 6)
        self.assertEqual(self.vector.get_product(), 6)
        self.assertEqual(self.vector.get_average(), 2)
        self.assertEqual(self.vector.get_min(), 1)
        self.assertEqual(self.vector.get_max(), 3)
