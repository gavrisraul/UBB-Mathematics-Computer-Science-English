#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
Plane class Passenger class
"""

from operator import mul
from functools import reduce


class Plane(object):
    """
    Plane class
    """

    def __init__(self, name, number, company, seats, destination, passengers):
        """
        Constructor for Plane class
        """
        self.__name = name
        self.__number = number
        self.__company = company
        self.__seats = seats
        self.__destination = destination
        self.__passengers = passengers

    def get_name(self):
        """
        name getter
        """
        return self.__name

    def set_name(self, new_name):
        """
        name setter
        """
        self.__name = name

    def get_number(self):
        """
        number getter
        """
        return self.__number

    def set_number(self, new_number):
        """
        number setter
        """
        self.__number = new_number

    def get_company(self):
        """
        company getter
        """
        return self.__company

    def set_company(self, new_company):
        """
        company setter
        """
        self.__company = new_company

    def get_seats(self):
        """
        seats getter
        """
        return self.__seats

    def set_seats(self, new_seats):
        """
        seats setter
        """
        self.__seats = new_seats

    def get_destination(self):
        """
        destination getter
        """
        return self.__destination

    def set_destination(self, new_destination):
        """
        destination setter
        """
        self.__destination = new_destination

    def get_passengers(self):
        """
        passengers getter
        """
        return self.__passangers

    def set_passengers(self, new_passangers):
        """
        passengers setter
        """
        self.__passangers = new_passangers

    def __str__(self):
        """Get the string representation of a plane."""
        return (
            f"( {self.__name}, "
            f"{self.__number}, "
            f"{self.__company}, "
            f"{self.__seats}, "
            f"{self.__destination}, "
            f"{self.__passengers} )"
        )


class Passenger(object):
    """
    Passenger class
    """

    def __init__(self, first_name, last_name, passport_number):
        """
        Constructor for Passenger class
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_number = passport_number

    def get_first_name(self):
        """
        first name getter
        """
        return self.__first_name

    def set_first_name(self, new_first_name):
        """
        first name setter
        """
        self.__first_name = new_first_name

    def get_last_name(self):
        """
        last name getter
        """
        return self.__last_name

    def set_last_name(self, new_last_name):
        """
        last name setter
        """
        self.__last_name = new_last_name

    def get_passport_number(self):
        """
        passport number getter
        """
        return self.__passport_number

    def set_passport_number(self, new_passport_number):
        """
        passport number setter
        """
        self.__passport_number = new_passport_number

    def __str__(self):
        """
        Get the string representation of a passanger
        """
        return f"({self.__first_name}, {self.__last_name}, {self.__passport_number})"
