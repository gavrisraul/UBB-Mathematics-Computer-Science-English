#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
TestPointRepository class
"""


import unittest
from domain.point import MyPoint
from infrastructure.pointrepo import PointRepository


class TestPointRepository(unittest.TestCase):
    """
    Testing PointRepository class. It uses unittest.TestCase
    """

    def setUp(self):
        """
        Lets make a setup
        """
        self.repo = PointRepository()
        self.first_point = MyPoint(coord_x=1, coord_y=2, color="red")
        self.second_point = MyPoint(coord_x=4, coord_y=3, color="blue")

    def tearDown(self):
        """
        Delete these
        """
        del (self.repo)
        del (self.first_point)
        del (self.second_point)

    def test_add(self):
        """
        testing add
        """
        self.assertEqual(self.repo.points, [])

        self.repo.addnewbycoords(self.first_point)
        self.assertTrue(self.repo.points)
        self.assertIs(self.repo.points[0], self.first_point)

        self.repo.addnewbycoords(self.second_point)
        self.assertTrue(self.repo.points)
        self.assertIs(self.repo.points[0], self.first_point)
        self.assertIs(self.repo.points[1], self.second_point)

    def test_get_methods(self):
        """
        testing get methods
        """
        self.repo.addnewbycoords(self.first_point)
        self.repo.addnewbycoords(self.second_point)

        self.assertIs(self.repo.getallpoints(), self.repo.points)

        self.assertIs(self.repo.getbycolor("red"), self.first_point)
        self.assertIs(self.repo.getbyindex(1), self.second_point)

    def test_update_methods(self):
        """
        testing update
        """
        self.repo.updatepointatindex(1, 3, 3, "blue")
        self.assertTrue(self.repo.points[1] == MyPoint(3, 3, "blue"))

    def test_delete_methods(self):
        """
        testing delete
        """
        self.repo.addnewbycoords(self.first_point)
        self.repo.addnewbycoords(self.second_point)

        self.repo.deletebyindex(0)
        self.assertIs(self.second_point, self.repo.points[0])

        self.repo.deletebycoords(4, 3)
        self.assertEqual(self.repo.points, [])
