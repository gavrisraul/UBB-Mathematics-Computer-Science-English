#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
TestVectorRepository class
"""


import unittest
from domain.business import MyVector
from infrastructure.repository import VectorRepository


class TestVectorRepository(unittest.TestCase):
    """
    TestVectorRepository. It uses unittest.TestCase
    """

    def setUp(self):
        """
        Lets make a setup
        """
        self.repo = VectorRepository()
        self.vector = MyVector(name="Raul", color="r", _type=1, values=[1, 2, 3])
        self.second_vector = MyVector(name="Alex", color="b", _type=2, values=[4, 5, 6])

    def tearDown(self):
        """
        Delete these
        """
        del self.repo
        del self.vector
        del self.second_vector

    def test_add(self):
        """
        Testing add
        """
        self.assertEqual(self.repo.vectors, [])

        self.repo.add_vector(self.vector)
        self.assertTrue(self.repo.vectors)
        self.assertIs(self.repo.vectors[0], self.vector)

        self.repo.add_vector(self.second_vector)
        self.assertTrue(self.repo.vectors)
        self.assertIs(self.repo.vectors[0], self.vector)
        self.assertIs(self.repo.vectors[1], self.second_vector)

    def test_get_metods(self):
        """
        Testing get
        """
        self.repo.add_vector(self.vector)
        self.repo.add_vector(self.second_vector)

        self.assertIs(self.repo.get_by_name("Raul"), self.vector)
        self.assertIs(self.repo.get_by_name("Alex"), self.second_vector)

        self.assertIs(self.repo.get_index(0), self.vector)
        self.assertIs(self.repo.get_index(1), self.second_vector)

    def test_update_methods(self):
        """
        Testing update
        """
        self.repo.update_vector(self.vector, "Batman", "b", [5, 6, 7, 8], 10)
        self.assertTrue(self.vector.name == "Batman")
        self.assertTrue(self.vector.color == "b")
        self.assertTrue(self.vector.type == 10)
        self.assertTrue(all([x in self.vector.values for x in [5, 6, 7, 8]]))
        self.assertTrue(len(self.vector.values) == 4)

        self.repo.add_vector(self.vector)
        self.repo.add_vector(self.second_vector)

        self.repo.update_index(1, "Robin", "y", [15, 16, 17, 18, 19], 11)
        tested_vector = self.repo.get_index(1)
        self.assertTrue(tested_vector.name == "Robin")
        self.assertTrue(tested_vector.color == "y")
        self.assertTrue(tested_vector.type == 11)
        self.assertTrue(all([x in tested_vector.values for x in [15, 16, 17, 18, 19]]))
        self.assertTrue(len(tested_vector.values) == 5)
        self.assertIs(self.second_vector, tested_vector)

        self.repo.update_by_name("Batman", "Robin", "r", [1], 1)
        second_tested_vector = self.repo.get_index(0)
        self.assertTrue(second_tested_vector.name == "Robin")
        self.assertTrue(second_tested_vector.color == "r")
        self.assertTrue(second_tested_vector.type == 1)
        self.assertTrue(all([x in second_tested_vector.values for x in [1]]))
        self.assertTrue(len(second_tested_vector.values) == 1)
        self.assertIs(self.vector, second_tested_vector)

    def test_delete_methods(self):
        """
        Testing delete
        """
        self.repo.add_vector(self.vector)
        self.repo.add_vector(self.second_vector)

        self.repo.delete_by_index(0)
        self.assertIs(self.second_vector, self.repo.vectors[0])

        self.repo.delete_by_name("Alex")
        self.assertEqual(self.repo.vectors, [])
