#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
TestDomain class
"""

import unittest

from domain.business import Passenger, Plane


class TestPlane(unittest.TestCase):
    def setUp(self):
        self.plane = Plane(
            name="lol",
            number=4141,
            company="Cluj Airlines",
            seats=888,
            destination="cluj",
            passengers=[],
        )

    def test_attributes(self):
        self.assertEqual(self.plane.name, "lol")
        self.assertEqual(self.plane.number, 4141)
        self.assertEqual(self.plane.company, "Cluj Airlines")
        self.assertEqual(self.plane.destination, "cluj")


class TestPassanger(unittest.TestCase):
    def setUp(self):
        self.passanger = Passanger(
            first_name="lol1", last_name="lol2", passport_number=4141
        )

    def test_attributes(self):
        self.assertEqual(self.passanger.first_name, "lol1")
        self.assertEqual(self.passanger.last_name, "lol2")
        self.assertEqual(self.passanger.passport_number, 4141)
