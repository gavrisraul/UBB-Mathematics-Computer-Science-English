#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
Controller class
"""

from infrastructure.repository import VectorRepository


class Controller(object):
    """
    Controller class
    """

    def __init__(self, repo=None):
        """
        Constructor for controller class
        """
        self.repo = VectorRepository()

    def add_vector_ctrl(self, name, color, _type, values):
        """
        Add a new vector controller
        """
        self.repo.add_vector(name, color, _type, values)

    def get_all_ctrl(self):
        """
        Return all points in the repo
        """
        return self.repo.vectors

    def get_by_index_ctrl(self, index):
        """
        Get a vector by its index
        """
        return self.repo.get_index(index)

    def update_by_index_ctrl(self, index, name_id, color, values, _type):
        """
        Update a vector at a given index
        """
        self.repo.update_index(index, name_id, color, values, _type)

    def update_by_name_id_ctrl(self, name_id, name, color, values, _type):
        """
        Update a vector with a given name id
        """
        self.repo.update_by_name(
            name=name, name_id=name_id, color=color, values=values, _type=_type
        )

    def delete_by_index_ctrl(self, index):
        """
        Delete vector by index
        """
        self.repo.delete_by_index(index)

    def delete_by_name_ctrl(self, name):
        """
        Delete vector by name id
        """
        self.repo.delete_by_name(name)

    def plot_ctrl(self):
        """
        Plot all vectors using matplotlib
        """
        print("Function not found!")

    def get_repository_elements_sum_ctrl(self):
        """
        Get the sum of all elements of all vectors in the repository
        """
        return self.repo.get_repository_elements_sum()

    def get_repository_vector_sum_ctrl(self):
        """
        Get the sum of all vectors in the repository as a vector
        """
        return self.repo.get_repository_vector_sum()

    def get_vectors_that_have_sum_ctrl(self, expected_sum):
        """
        Get a list of vectors having the sum equal to the given value
        """
        return self.repo.get_vectors_that_have_sum(expected_sum)

    def get_vectors_with_min_less_than_ctrl(self, limit):
        """
        Get a list of vectors having the mininum less than the given
        value
        """
        return self.repo.get_vectors_with_min_less_than(limit)

    def get_vectors_with_color_ctrl(self, color):
        """
        Get the sum of elements of vectors that have the given color
        """
        return self.repo.get_vectors_with_color(color)

    def get_sum_of_vectors_with_sum_gt_ctrl(self, limit):
        """
        Get the sum of elements of vectors that have the given color
        """
        return self.repo.get_max_of_vectors_with_sum_gt(limit)

    def get_min_of_all_vectors_ctrl(self):
        """
        Return the minimum of all vectors
        """
        return self.repo.get_min_of_all_vectors()

    def get_dot_product_of_consecutive_vectors_ctrl(self):
        """
        Get the dot product of consecutive vectors in the array
        """
        return self.repo.get_dot_product_of_consecutive_vectors()

    def delete_all_vectors_ctrl(self):
        """
        Empty the vector repository
        """
        self.repo.delete_all_vectors()

    def delete_by_color_ctrl(self, color):
        """
        Delete vectors that have a given color
        """
        self.repo.delete_by_color(color)

    def delete_by_prod_ctrl(self, prod):
        """
        Delete all vectors that have a product greater than a given
        """
        self.repo.delete_by_prod(prod)

    def delete_between_indexes_ctrl(self, start, end):
        """
        Delete vectors between two indexes
        """
        self.repo.delete_between_indexes(start, end)

    def delete_by_max_value_ctrl(self, max_value):
        """
        Delete vectors that have a given maximum value
        """
        self.repo.delete_by_max_value(max_value)

    def add_to_all_ctrl(self, scalar):
        """
        Add a scalar to all vectors
        """
        self.repo.add_to_all(scalar)

    def update_color_by_name_ctrl(self, name, color):
        """
        Update the color of a vector identified by a given name
        """
        self.repo.update_color_by_name(name, color)

    def update_by_type_set_color_ctrl(self, _type, color):
        """
        Update all vectors of a given type by changing their color
        """
        self.repo.update_by_type_set_color(_type, color)
