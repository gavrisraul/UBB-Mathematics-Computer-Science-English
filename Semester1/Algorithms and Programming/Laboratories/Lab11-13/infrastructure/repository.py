#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
PlaneRepository class PassengerRepository class
"""

from domain.business import Plane, Passenger
from infrastructure.utils import (
    sort_by_function,
    filter_by_function,
    search_by_function,
    get_combinations,
)


class PlaneRepository(object):
    """
    PlaneRespository class
    """

    def __init__(self, planes=None):
        """
        Constructor for PlaneRepository
        """
        if not planes:
            planes = []

        self.__planes = planes

    def add_plane(self, name, number, company, seats, destination, passengers):
        """
        Add a new plane to the repo
        """
        if self.get_by_name(name):
            raise ValueError("Plane aleardy exists")

        self.__planes.append(
            Plane(name, number, company, seats, destination, passengers)
        )

    def get_planes(self):
        """
        Get all planes from repository
        """
        return self.__planes

    def set_planes(self, planes):
        """
        Set all planes from repository
        """
        self.__planes = planes

    def get_by_name(self, name):
        """
        Helper method for getting a plane by name
        """
        for plane in self.__planes:
            if plane.get_name() == name:
                return plane

    def get_index(self, index):
        """
        Get plane at index
        """
        return self.__planes[index]

    @staticmethod
    def update_plane(plane, name, number, company, seats, destination, passengers):
        """
        Helper method for updating a plane
        """
        plane.set_name(name)
        plane.set_number(number)
        plane.set_company(company)
        plane.set_seats(seats)
        plane.set_destination(destination)
        plane.set_passengers(passengers)

    def update_index(
        self, index, name, number, company, seats, destination, passengers
    ):
        """
        Update plane at index
        """
        self.update_plane(
            self.__planes[index], name, number, company, seats, destination, passengers
        )

    def update_by_name(
        self, name, index, name, number, company, seats, destination, passengers
    ):
        """
        Update a plane by name
        """
        for plane in self.__planes:
            if plane.get_name() == name:
                self.update_plane(
                    plane, index, name, number, company, seats, destination, passengers
                )
                break

    def delete_by_index(self, index):
        """
        Delete a plane by index
        """
        if index < 0 or index >= len(self.__planes):
            raise ValueError

        self.__planes.pop(index)

    def delete_by_name(self, name):
        """
        Delete a plane by name
        """
        del_index = -1
        for index, plane in enumerate(self.__planes):
            if plane.get_name() == name:
                del_index = index

        if del_index == -1:
            raise ValueError("Name not in array!")

        self.delete_by_index(del_index)

    def delete_all_planes(self):
        """
        Empty the plane repository
        """
        while self.__planes:
            self.__planes.pop()

    def delete_between_indexes(self, start, end):
        """
        Delete plane lanes between two indexes
        """
        self.__planes = (
            self.__planes[0:start] + self.__planes[end : len(self.__planes) - 1]
        )

    def sort_passangers_by_lastname(self, plane):
        """
        Sort all passengers in a plane by lastname
        """
        plane.passengers = sort_by_function(
            plane.passengers, lambda x, y: x.last_name <= y.last_name
        )
        """plane.set_passengers(sort_by_function(plane.get_passengers, lambda x, y: x.get_last_name() <= y.get_last_name()))"""

    def sort_planes_by_number_of_passengers(self):
        """
        Sort all pplanes by number of passengers
        """
        self.__planes = sort_by_function(
            self.__planes, lambda x, y: len(x.passengers) <= len(y.passengers)
        )

    def sort_planes_by_number_of_pass_named_starting_with(self, substring):
        """
        Sort all planes by number of passengers whose name starts with substring
        """

        def get_pass_nr(plane, substring):
            return len(
                [
                    p
                    for p in plane.get_passengers()
                    if p.get_first_name().startswith(substring)
                ]
            )

        return sort_by_function(
            self.__planes, lambda x, y: get_pass_nr(x) <= get_pass_nr(y)
        )

    def sort_planes_by_destination_and_passengers(self, plane):
        """
        Sort all planes by length of passengers + destination
        """

        def get_sort_string(plane):
            return str(len(plane.get_passengers())) + plane.get_destination()

        return sort_by_function(
            plane.get_passengers(),
            lambda x, y: get_sort_string(x) <= get_sort_string(y),
        )

    def find_planes_with_passengers_with_weird_passports(self):
        """
        Find planes that have passengers whose passport starts with the same
        3 digits
        """

        def respspects_that_condition(plane):
            return any(
                [
                    p.get_passport_number()[0] == p.get_passport_number()[1]
                    and p.get_passport_number()[1] == p.get_passport_number()[2]
                    for p in plane.get_passengers()
                ]
            )

        return filter_by_function(self.__planes, respspects_that_condition)

    def find_passengers_from_plane(self, plane, substring):
        """
        Find passengers from plane that have a given substring in their name
        """
        return filter_by_function(
            plane.get_passengers(),
            lambda x: substring in x.get_first_name() or substring in x.get_last_name(),
        )

    def find_planes_with_passenger(self, name):
        """
        Find all planes that have a passenger with a given name
        """
        return filter_by_function(
            self.__planes,
            lambda x: any(
                filter_by_function(
                    x.get_passengers(),
                    lambda y: name in y.get_first_name() + " " + y.get_last_name(),
                )
            ),
        )

    def make_groups(self, k):
        """
        Make groups of k planes with the same destination but belonging to different airline companies
        """
        destinations = set([p.get_destination() for p in self.__planes])
        planes_grouped_by_destination = {}
        for dest in destinations:
            planes_grouped_by_destination[dest] = filter_by_function(
                self.__planes, lambda x: x.dest == dest
            )

        groups = {}
        for dest, planes in planes_grouped_by_company.items():
            groups[dest] = get_combinations(planes, k)

        return groups


class PassengerRepository(object):
    """
    PassengerRepository class
    """

    def __init__(self, passengers=None):
        """
        Constructor for PassengerRepository class
        """
        if not passengers:
            passengers = []

        self.__passengers = passengers

    def add_passenger(self, first_name, last_name, passport_number):
        """
        Add a new passanger to the repo
        """
        if self.get_by_name(first_name) and self.get_by_name(last_name):
            raise ValueError("Passanger aleardy exists")

        self.__passengers.append(Passenger(first_name, last_name, passport_number))

    def get_passengers(self):
        """
        Get all passengers from repository
        """
        return self.__passengers

    def set_passengers(self, passengers):
        """
        Set all passengers from repository
        """
        self.__passengers = passengers

    def get_by_name(self, first_name, last_name):
        """
        Helper method for getting a passanger by name
        """
        for passenger in self.__passengers:
            if (
                passenger.get_first_name() == first_name
                and passenger.get_last_name() == last_name
            ):
                return passenger

    def get_index(self, index):
        """
        Get passanger at index
        """
        return self.__passengers[index]

    def update_passanger(passenger, first_name, last_name, passport_number):
        """
        Helper method for updating a passenger
        """
        passenger.set_first_name(first_name)
        passenger.set_last_name(last_name)
        passenger.set_passport_number(passport_number)

    def update_index(self, index, passenger, first_name, last_name, passport_number):
        """
        Update passenger at index
        """
        self.update_passenger(
            self.__passengers[index], first_name, last_name, passport_number
        )

    def update_by_name(self, name1, name2, first_name, last_name, passport_number):
        """
        Update a passenger by name
        """
        for passenger in self.__passengers:
            if (passenger.get_first_name() == name1) and (
                passenger.get_last_name() == name2
            ):
                self.update_passenger(passenger, first_name, last_name, passport_number)
                break

    def delete_by_index(self, index):
        """
        Delete a passenger by index
        """
        if index < 0 or index >= len(self.__passengers):
            raise ValueError

        self.__passengers.pop(index)

    def delete_by_name(self, name1, name2):
        """
        Delete a passenger by name
        """
        del_index = -1
        for index, passenger in enumerate(self.__passengers):
            if (passenger.get_first_name == name1) and (
                passenger.get_last_name() == name2
            ):
                del_index = index

        if del_index == -1:
            raise ValueError("Name not in array!")

        self.delete_by_index(del_index)

    def delete_all_passengers(self):
        """
        Empty the passenger repository
        """
        while self.__passengers:
            self.__passengers.pop()

    def delete_between_indexes(self, start, end):
        """
        Delete passengers between two indexes
        """
        self.__passengers = (
            self.__passengers[0:start]
            + self.__passengers[end : len(self.__passengers) - 1]
        )

    def make_groups(self, k):
        """
        Make groups of k passengers from the same plane but with different last names
        """
        companies = set([p.company for p in self.__planes])
        planes_grouped_by_company = {}
        for company in companies:
            planes_grouped_by_company[company] = filter_by_function(
                self.__planes, lambda x: x.company == company
            )

        groups = {}
        for company, planes in planes_grouped_by_company.items():
            groups[company] = get_combinations(planes, k)

        return groups
