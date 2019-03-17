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

from infrastructure.repository import PlaneRepository, PassengerRepository


class Controller(object):
    """
    Controller class
    """

    def __init__(self, plane_repo=None, passenger_repo=None):
        """
        Constructor for Controller class
        """
        if not plane_repo:
            plane_repo = PlaneRepository()

        self.plane_repo = plane_repo

        if not passenger_repo:
            passenger_repo = PassengerRepository()

        self.passenger_repo = passenger_repo

    def plane_add_ctrl(self, name, number, company, seats, destination, passengers):
        """
        Add a new plane controller
        """
        self.plane_repo.add_plane(name, number, company, seats, destination, passengers)

    def passenger_add_ctrl(self, first_name, last_name, passport_number):
        """
        Add a new passenger controller
        """
        self.passenger_repo.add_passenger(first_name, last_name, passport_number)

    def plane_get_all_ctrl(self):
        """
        Return all planes in the repo
        """
        return self.plane_repo.__planes

    def passenger_get_all_ctrl(self):
        """
        Return all passengers in the repo
        """
        return self.passengers_repo.__passengers

    def plane_get_by_index_ctrl(self, index):
        """
        Get a plane by it's index
        """
        return self.plane_repo.get_index(index)

    def passenger_get_by_index_ctrl(self, index):
        """
        Get a passenger by it's index
        """
        return self.passenger_repo.get_index(index)

    def plane_update_by_index_ctrl(
        self, index, name, number, company, seats, destination, passengers
    ):
        """
        Update a plane at a given index
        """
        self.plane_repo.update_index(
            index, name, number, company, seats, destination, passengers
        )

    def passenger_update_by_index_ctrl(self, first_name, last_name, passport_number):
        """
        Update a passenger at a given index
        """
        self.passenger_repo.update_index(index, first_name, last_name, passport_number)

    def plane_update_by_name_id_ctrl(
        self, name_id, name, number, company, seats, destination, passengers
    ):
        """
        Update a plane with a given name id
        """
        self.plane_repo.update_by_name(
            name_id, name, number, company, seats, destination, passengers
        )

    def passenger_update_by_name_id_ctrl(
        self, name_id, first_name, last_name, passport_number
    ):
        """
        Update a passenger with a given name id
        """
        self.passenger_repo.update_by_name(
            name_id, first_name, last_name, passport_number
        )

    def plane_delete_by_index_ctrl(self, index):
        """
        Delete plane by index
        """
        self.plane_repo.delete_by_index(index)

    def passenger_delete_by_index_ctrl(self, index):
        """
        Delete passenger by index
        """
        self.passenger_repo.delete_by_index(index)

    def plane_delete_by_name_ctrl(self, name):
        """
        Delete plane by name id
        """
        self.plane_repo.delete_by_name(name)

    def passenger_delete_by_name_ctrl(self, name):
        """
        Delete passenger by name id
        """
        self.passenger_repo.delete_by_name(name)

    def plane_delete_all_ctrl(self):
        """
        Empty the plane repository
        """
        self.plane_repo.delete_all_planes()

    def passenger_delete_all_ctrl(self):
        """
        Empty the passenger repository
        """
        self.passenger_repo.delete_all_passengers()

    def plane_delete_between_indexes_ctrl(self, start, end):
        """
        Delete planes between two indexes
        """
        self.plane_repo.delete_between_indexes(start, end)

    def passenger_delete_between_indexes_ctrl(self, start, end):
        """
        Delete passengers between two indexes
        """
        self.passenger_repo.delete_between_indexes(start, end)

    def sort_passengers_by_lastname_ctrl(self, plane_name):
        """
        Sort all passengers in a plane by lastname
        """
        self.plane_repo.sort_passengers_by_lastname(plane_name)

    def sort_planes_by_number_of_passengers_ctrl(self):
        """
        Sort all pplanes by number of passangers
        """
        self.plane_repo.sort_planes_by_number_of_passengers()

    def sort_planes_by_number_of_pass_named_starting_with_ctrl(self, substring):
        """
        Sort all planes by number of passengers whose name starts with substring
        """
        self.plane_repo.sort_planes_by_number_of_pass_named_starting_with(substring)

    def sort_planes_by_destination_and_passengers_ctrl(self, plane):
        """
        Sort all planes by length of passengers + destination
        """
        self.plane_repo.sort_planes_by_destination_and_passengers(plane)

    def find_planes_with_passengers_with_weird_passports_ctrl(self):
        """
        Find planes that have passengers whose passport starts with the same
        3 digits
        """
        return self.plane_repo.find_planes_with_passengers_with_weird_passports()

    def find_passengers_from_plane_ctrl(self, plane, substring):
        """
        Find passengers from plane that have a given substring in their name
        """
        return self.plane_repo.find_passengers_from_plane(plane, substring)

    def find_planes_with_passenger_ctrl(self, name):
        """
        Find all planes that have a passenger with a given name
        """
        return self.plane_repo.find_planes_with_passenger(name)

    def plane_make_groups(self):
        """
        Make groups of k planes with the same destination but belonging to different airline companies
        """
        return self.plane_repo.make_groups()

    def passenger_make_groups(self):
        """
        Make groups of k passengers from the same plane but with different last names
        """
        return self.passenger_repo.make_groups()
