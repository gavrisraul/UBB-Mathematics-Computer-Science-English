#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
Ui class
"""

from application.controller import Controller


class Ui(object):
    def __init__(self, controller=None):
        controller = Controller()

        self.controller = controller
        self.options = {
            1: self.add_plane_submenu,
            2: self.add_passenger_submenu,
            3: self.plane_get_all_submenu,
            4: self.passenger_get_all_submenu,
            5: self.plane_get_by_index_submenu,
            6: self.passenger_get_by_index_submenu,
            7: self.plane_update_by_index_submenu,
            8: self.passenger_update_by_index,
            9: self.plane_update_by_name_id_submenu,
            10: self.passenger_update_by_name_id_submenu,
            11: self.plane_delete_by_index_submenu,
            12: self.passenger_delete_by_index_submenu,
            13: self.plane_delete_by_name_submenu,
            14: self.passenger_delete_by_name_submenu,
            15: self.plane_delete_all_submenu,
            16: self.passenger_delete_all_submenu,
            17: self.plane_delete_between_indexes_submenu,
            18: self.passenger_delete_between_indexes_submenu,
            19: self.exit_submenu,
        }

    def add_plane_submenu(self):
        """
        add_plane_submenu
        """
        name = input("Enter plane name id: ")
        number = input("Enter number: ")
        seats = int(input("Enter number of seats: "))
        company = input("Enter company")
        destination = input("Enter destination")

        self.controller.plane_add_ctrl(
            name, number, company, seats, destination, [])

        pas_nr = int(input('How many passengers do you want to add?'))
        for i in range(pas_nr):
            self.add_passenger_submenu(
                self.controller.plane_get_by_index_ctrl(-1))

    def add_passenger_submenu(self):
        """
        add_passenger_submenu
        """
        first_name = input("Enter first_name: ")
        last_name = input("Enter last_name: ")
        passport_number = input("Enter passport_number: ")

        self.controller.passenger_add_ctrl(
            first_name, last_name, passport_number)

        if p:
            p.passengers.append(
                self.controller.passenger_get_by_index_ctrl(-1))

    def plane_get_all_submenu(self):
        """
        plane_get_all_submenu
        """
        pass

    def passenger_get_all_submenu(self):
        """
        passenger_get_all_submenu
        """
        pass

    def plane_get_by_index_submenu(self):
        """
        plane_get_by_index_submenu
        """
        print(self.controller.plane_get_by_index_ctrl(
            int(input("Enter index: "))))

    def passenger_get_by_index_submenu(self):
        """
        passenger_get_by_index_submenu
        """
        print(self.controller.passenger_get_by_index_ctrl(
            int(input("Enter index: "))))

    def plane_update_by_index_submenu(self):
        """
        plane_update_by_index_submenu
        """
        pass

    def passenger_update_by_index(self):
        """
        passenger_update_by_index
        """
        pass

    def plane_update_by_name_id_submenu(self):
        """
        plane_update_by_name_id_submenu
        """
        name = input("Enter index name: ")
        name_id = input("Enter new_name: ")
        number = input("Enter number: ")
        seats = int(input("Enter number of seats: "))
        destination = int(input("Enter destination"))
        company = int(input("Enter company"))

        self.controller.plane_update_by_name_id_ctrl(
            name=name,
            name_id=name_id,
            number=number,
            seats=seats,
            company=company,
            destination=destination,
            passengers=[]
        )

        pas_nr = int(input('How many passangers do you want to add?'))
        for i in range(pas_nr):
            self.add_passenger_submenu(
                self.controller.plane_get_by_index_ctrl(-1))

    def passenger_update_by_name_id_submenu(self):
        """
        passenger_update_by_name_id_submenu
        """
        name = input("Enter index name: ")
        first_name = input("Enter first_name: ")
        last_name = input("Enter last_name: ")
        passport_number = int(input("Enter passport_number: "))

        self.controller.passenger_update_by_name_id_ctrl(
            name_id, first_name, last_name, passport_number)

    def plane_delete_by_index_submenu(self):
        """
        plane_delete_by_index_submenu
        """
        self.controller.plane_delete_by_index_ctrl(int(input("Enter index: ")))

    def passenger_delete_by_index_submenu(self):
        """
        passenger_delete_by_index_submenu
        """
        self.controller.passenger_delete_by_index_ctrl(
            int(input("Enter index: ")))

    def plane_delete_by_name_submenu(self):
        """
        plane_delete_by_name_submenu
        """
        pass

    def passenger_delete_by_name_submenu(self):
        """
        passenger_delete_by_name_submenu
        """
        pass

    def plane_delete_all_submenu(self):
        """
        plane_delete_all_submenu
        """
        pass

    def passenger_delete_all_submenu(self):
        """
        passenger_delete_all_submenu
        """
        pass

    def plane_delete_between_indexes_submenu(self):
        """
        plane_delete_between_indexes_submenu
        """
        pass

    def passenger_delete_between_indexes_submenu(self):
        """
        passenger_delete_between_indexes_submenu
        """
        pass

    def sort_passengers_by_lastname_submenu(self):
        """
        Sort all passengers in a plane by lastname
        """
        self.controller.sort_passengers_by_lastname_ctrl('Enter plane_name: '):

    def sort_planes_by_number_of_passengers_submenu(self):
        """
        Sort all planes by number of passengers
        """
        self.controller.sort_planes_by_number_of_passengers_ctrl()

    def sort_planes_by_number_of_pass_named_starting_with_submenu(self):
        """
        Sort all planes by number of passengers whose name starts with substring
        """
        self.controller.sort_planes_by_number_of_pass_named_starting_with_ctrl(
            'Enter substring: ')

    def sort_planes_by_destination_and_passengers_submenu(self):
        """
        Sort all planes by length of passengers + destination
        """
        self.controller.sort_planes_by_destination_and_passengers_ctrl(
            'Enter plane name:')

    def find_planes_with_passengers_with_weird_passports_submenu(self):
        """
        Find planes that have passengers whose passport starts with the same
        3 digits
        """
        print(
            self.controller.find_planes_with_passengers_with_weird_passports_ctrl()
        )

    def find_passengers_from_plane_submenu(self, plane, substring):
        """
        Find passengers from plane that have a given substring in their name
        """
        print(
            self.controller.find_passengers_from_plane_ctrl(
                self.controller.plane_get_by_index_ctrl(
                    int(input("Enter plane index: "))),
                input('Enter substring')
            )
        )

    def find_planes_with_passenger_submenu(self):
        """
        Find all planes that have a passenger with a given name
        """
        print(
            self.controller.find_planes_with_passenger_ctrl(
                input('Enter name: '))
        )

    def exit_submenu(self):
        """
        Exit the app
        """
        exit()

    def run(self):
        """
        Running the app and cycle through options
        """
        while True:
            print("\n" * 2 + "Option:")

            for number, function in self.options.items():
                print(f"\t{number}\t:::\t{function.__doc__}")
            print("\n")

            try:
                selected = int(input("Option number: "))
            except Exception as e:
                print(f"Error, enter a valid option number!" "{str(e)}")
                continue

            print(f"\nCalling {self.options[selected].__name__}..,\n\n")
            print("======================")
            try:
                self.options[selected]()
            except SystemExit:
                raise
            except Exception as e:
                print(e)
                print(
                    f"Something went wrong in "
                    "{self.options[selected].__name__}! Try again.."
                )
            print("======================")
