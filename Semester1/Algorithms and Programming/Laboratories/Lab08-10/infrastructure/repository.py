#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
VectorRepository class
"""


from functools import reduce
from domain.business import MyVector


class VectorRepository(object):
    """
    VectorRepository class
    """

    def __init__(self, vectors=[]):
        self.__vectors = vectors

    def add_vector(self, name, color, _type, values):
        """
        Add a new vector to the repo
        """
        if self.get_by_name(name):
            raise ValueError("Vector aleardy exists")
        self.vectors.append(MyVector(name, color, _type, values))

    @property
    def vectors(self):
        """
        Get all vectors from repository
        """
        return self.__vectors

    @vectors.setter
    def vectors(self, vectors):
        self.__vectors = vectors

    def get_by_name(self, name):
        """
        Helper method for getting a vector by name
        """
        for vector in self.vectors:
            if vector.get_name() == name:
                return vector

    def get_index(self, index):
        """
        Get vector at index
        """
        return self.vectors[index]

    @staticmethod
    def update_vector(vector, name, color, values, _type):
        """
        Helper method for updating a vector
        """
        vector.set_name(name)
        vector.set_color(color)
        vector.set_values(values)
        vector.set_type(_type)

    def update_index(self, index, name_id, color, values, _type):
        """
        Update vector at index
        """
        self.update_vector(self.vectors[index], name_id, color, values, _type)

    def update_by_name(self, name, name_id, color, values, _type):
        """
        Update a vector by name
        """
        for vector in self.vectors:
            if vector.get_name() == name:
                self.update_vector(vector, name_id, color, values, _type)
                break

    def delete_by_index(self, index):
        """
        Delete a vector by index
        """
        if index < 0 or index >= len(self.vectors):
            raise ValueError
        self.vectors.pop(index)

    def delete_by_name(self, name):
        """
        Delete a vector by name
        """
        del_index = -1
        for index, vector in enumerate(self.vectors):
            if vector.get_name() == name:
                del_index = index
        if del_index == -1:
            raise ValueError("Name not in array!")
        self.delete_by_index(del_index)

    def plot(self):
        """
        Plot all vectors to chart
        """
        pass

    def get_repository_elements_sum(self):
        """
        Get the sum of all elements of all vectors in the repository
        """
        return sum([x.get_sum() for x in self.vectors])

    def get_repository_vector_sum(self):
        """
        Get the sum of all vectors in the repository as a vector.
        We consider here a vector only the values of a MyVector instance
        """
        return reduce(lambda x, y: x + y, [x.get_values() for x in self.vectors])

    def get_vectors_that_have_sum(self, expected_sum):
        """
        Get a list of vectors having the sum equal to the given value
        """
        return [x for x in self.vectors if x.get_sum() == expected_sum]

    def get_vectors_with_min_less_than(self, minimum_limit):
        """
        Get a list of vectors having the mininum less than the given
        value
        """
        return [x for x in self.vectors if x.get_min() < minimum_limit]

    def get_vectors_with_color(self, color):
        """
        Get the sum of elements of vectors that have the given color
        """
        return sum([x.get_sum() for x in self.vectors if x.get_color() == color])

    def get_max_of_vectors_with_sum_gt(self, sum_limit):
        """
        Get the max of elements of vector that has sum gt given value
        """
        if len(self.vectors) == 0:
            return
        biggest_vector = self.vectors[0]
        for vector in self.vectors[1:]:
            if biggest_vector.sum() < vector.sum():
                biggest_vector = vector
        return biggest_vector.get_max()

    def get_min_of_all_vectors(self):
        """
        Return the minimum of all vectors
        """
        return min([x.get_min() for x in self.vectors])

    def get_dot_product_of_consecutive_vectors(self):
        """
        Get the dot product of consecutive vectors in the array
        """
        dot_products_list = []
        index = 1
        while index < len(self.vectors):
            try:
                current_prod = self.vectors[index] * self.vectors[index - 1]
            except:
                raise ValueError("Vectors don't have the same length!")
            dot_products_list.append(current_prod)
            index += 1
        return dot_products_list

    def delete_all_vectors(self):
        """
        Empty the vector repository
        """
        while self.vectors:
            self.vectors.pop()

    def delete_by_color(self, color):
        """
        Delete vectors that have a given color
        """
        self.vectors = [x for x in self.vectors if x.get_color() != color]

    def delete_by_prod(self, product):
        """
        Delete all vectors that have a product greater than a given
        """
        self.vectors = [x for x in self.vectors if x.get_product() > product]

    def delete_between_indexes(self, start, end):
        """
        Delete vectors between two indexes
        """
        self.vectors = self.vectors[0:start] + self.vectors[end : len(self.vectors) - 1]

    def delete_by_max_value(self, max_value):
        """
        Delete vectors that have a given maximum value
        """
        self.vectors = [x for x in self.vectors if x.get_max() != max_value]

    def add_to_all(self, scalar):
        """
        Add a scalar to all vectors
        """
        self.vectors = [x + scalar for x in self.vectors]

    def update_color_by_name(self, name, new_color):
        """
        Update the color of a vector identified by a given name
        """
        for v in self.vectors:
            if v.get_name() == name:
                v.set_color(new_color)
                return

    def update_by_type_set_color(self, _type, new_color):
        """
        Update all vectors of a given type by changing their color
        """
        for v in self.vectors:
            if v.get_type() == _type:
                v.set_color(new_color)
                return
