#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
MyVector class
"""


from operator import mul
from functools import reduce
import numpy as np


class MyVector(object):
    """
    MyVector class
    """

    def __init__(self, name="Raul", color="r", _type=1, values=[]):
        """
        Constructor for MyVector class
        """
        self.__name = name
        self.__color = color
        self.__type = _type
        self.__values = values

    def get_name(self):
        """
        getter for name
        """
        return self.__name

    def set_name(self, new_name):
        """
        setter for name
        """
        if type(new_name) not in (str, int):
            raise ValueError("Invalid name id!")
        self.__name = new_name

    def get_color(self):
        """
        getter for color
        """
        return self.__color

    def set_color(self, new_color):
        """
        setter for color
        """
        if new_color not in ("r", "g", "b", "y"):
            raise ValueError("Invalid color!")
        self.__color = new_color

    def get_type(self):
        """
        getter for type
        """
        return self.__type

    def set_type(self, new_type):
        """
        setter for type
        """
        if type(new_type) is not int or new_type < 1:
            raise ValueError("Invalid type!")
        self.__type = new_type

    def get_values(self):
        """
        getter for values
        """
        return self.__values

    def set_values(self, new_values):
        """
        setter for values
        """
        is_np_array = isinstance(new_values, np.ndarray)
        only_ints = all([isinstance(x, int) for x in new_values])
        if is_np_array is False and only_ints is False:
            raise ValueError("Invalid values!")
        if is_np_array:
            self.set_values(new_values)
        else:
            self.set_values(np.array(new_values))

    def __add__(self, other):
        """
        Add a scalar to a vector or add two vectors
        """
        if type(other) in (int, float):
            new_val = self.get_values()
            new_val += other
            self.set_values(new_val)
        elif type(other) is MyVector:
            new_val = self.get_values()
            new_val += other.values
            self.set_values(new_val)

    def __sub__(self, other):
        """
        Substract a scalar from a vector or substract two vectors
        """
        if type(other) in (int, float):
            new_val = self.get_values()
            new_val -= other
            self.set_values(new_val)
        elif type(other) is MyVector:
            new_val = self.get_values()
            new_val += other.values
            self.set_values(new_val)

    def __mul__(self, other):
        """
        Multiply a vector by a scalar or two vectors
        """
        if type(other) in (int, float):
            new_val = self.get_values()
            new_val *= other
            self.set_values(new_val)
        elif type(other) is MyVector:
            self.set_values(self.values.dot(other.values))

    def __str__(self):
        """
        Get the string representation of a vector
        """
        return f"Vector ({self.get_name()}, {self.get_color()}, {self.get_type()}, {self.get_values()})"

    def get_sum(self):
        """
        Get the sum of all the element in a vector
        """
        return sum(self.get_values())

    def get_product(self):
        """
        Get the product of all the element in a vector
        """
        return reduce(mul, self.get_values())

    def get_average(self):
        """
        Get the average of all the element in a vector
        """
        return self.get_sum() / float(len(self.get_values()))

    def get_min(self):
        """
        Get minimum of all the element in a vector
        """
        return min(self.get_values())

    def get_max(self):
        """
        Get maximum of all the element in a vector
        """
        return max(self.get_values())
