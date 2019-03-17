#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
Tests class
"""


import unittest
from domain.point import MyPoint


class MyPointTest(unittest.TestCase):
    """
    test class for domain MyPoint Class. It uses unittest.TestCase
    """

    def setUp(self):
        """
        Lets make a setup
        """
        self.first_point = MyPoint(coord_x=1, coord_y=2, color="red")
        self.second_point = MyPoint(coord_x=4, coord_y=3, color="blue")

    def test_attributes(self):
        """
        testing attributes for domain
        """
        self.assertTrue(self.first_point.get_coord_x() == 1)
        self.assertTrue(self.first_point.get_coord_y() == 2)
        self.assertTrue(self.first_point.get_color() == "red")
        self.assertTrue(self.second_point.get_coord_x() == 4)
        self.assertTrue(self.second_point.get_coord_y() == 3)
        self.assertTrue(self.second_point.get_color() == "blue")

    def test_operators(self):
        """
        testing operators
        """
        self.first_point.set_coord_x(3)
        self.assertTrue(self.first_point.get_coord_x() == 3)
        self.first_point.set_color("blue")
        self.assertTrue(self.first_point.get_color() == "blue")
