#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
MyPoint class gives coords for x and y in 2D space and its color representation
"""


class MyPoint(object):
    """
    MyPoint class
    """

    def __init__(self, coord_x, coord_y, color):
        """
        The initializaton of the class MyPoint which takes coord_x, coord_y, color
        """
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__color = color

    def get_coord_x(self):
        """
        Getter for coord_x
        """
        return self.__coord_x

    def set_coord_x(self, coord_x):
        """
        Setter for coord_x
        """
        self.__coord_x = coord_x

    def get_coord_y(self):
        """
        Getter for coord_y
        """
        return self.__coord_y

    def set_coord_y(self, coord_y):
        """
        Setter for coord_y
        """
        self.__coord_y = coord_y

    def get_color(self):
        """
        Getter for color
        """
        return self.__color

    def set_color(self, color):
        """
        Setter for color
        """
        self.__color = color

    def __repr__(self):
        """
        Representation for the object
        """
        return (
            "Point ("
            + str(self.__coord_x)
            + ", "
            + str(self.__coord_y)
            + ") of colour "
            + self.__color
            + "."
        )

    def __str__(self):
        """
        The format which should be displayed to the screen
        """
        return (
            "Point ("
            + str(self.__coord_x)
            + ", "
            + str(self.__coord_y)
            + ") of colour "
            + self.__color
            + "."
        )


# a = MyPoint(1, 2, "red")
# print(a)
