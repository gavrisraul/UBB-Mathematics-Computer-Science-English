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
    """
    Ui class
    """

    def __init__(self, controller=None):
        """
        Constructor for Ui class
        """
        controller = Controller()

        self.controller = controller
        self.options = {
            1: self.add_submenu,
            2: self.get_all_submenu,
            3: self.get_by_index_submenu,
            4: self.update_by_index_submenu,
            5: self.update_by_name_id_submenu,
            6: self.delete_by_index_submenu,
            7: self.delete_by_name_submenu,
            8: self.plot_submenu,
            9: self.get_repository_elements_sum_submenu,
            10: self.get_repository_vector_sum_submenu,
            11: self.get_vectors_that_have_sum_submenu,
            12: self.get_vectors_with_min_less_than_submenu,
            13: self.get_vectors_with_color_submenu,
            14: self.get_sum_of_vectors_with_sum_gt_submenu,
            15: self.get_min_of_all_vectors_submenu,
            16: self.get_dot_product_of_consecutive_vectors_submenu,
            17: self.delete_all_vectors_submenu,
            18: self.delete_by_color_submenu,
            19: self.delete_by_prod_submenu,
            20: self.delete_between_indexes_submenu,
            21: self.delete_by_max_value_submenu,
            22: self.add_to_all_submenu,
            23: self.update_color_by_name_submenu,
            24: self.update_by_type_set_color_submenu,
            25: self.exit_submenu,
        }

    def add_submenu(self):
        """
        Add a new vector
        """
        name = input("Enter vector name id: ")
        color = input("Enter vector color: ")
        _type = int(input("Enter vector type: "))
        len_vals = int(input("How many values do you want to add? "))

        values = []
        for _ in range(len_vals):
            values.append(int(input("Enter new value: ")))

        self.controller.add_vector_ctrl(name, color, _type, values)

    def get_all_submenu(self):
        """
        Return all points in the repo
        """
        print("\n".join([str(x) for x in self.controller.get_all_ctrl()]))

    def get_by_index_submenu(self):
        """
        Get a vector by its index
        """
        print(self.controller.get_by_index_ctrl(int(input("Enter index: "))))

    def update_by_index_submenu(self):
        """
        Update a vector at a given index
        """
        index = int(input("Enter index: "))
        name_id = input("Enter new name: ")
        color = input("Enter new color: ")
        values_len = int(input("How many values do you want to add? "))
        values = [int(input("Enter next value: ")) for _ in range(values_len)]
        _type = int(input("Enter the vector type: "))

        self.controller.update_by_index_ctrl(
            index=index, name_id=name_id, color=color, values=values, _type=_type
        )

    def update_by_name_id_submenu(self):
        """
        Update a vector with a given name id
        """
        name = input("Enter index name: ")
        name_id = input("Enter new_name: ")
        color = input("Enter new color: ")
        values_len = int(input("How many values do you want to add? "))
        values = [int(input("Enter next value: ")) for _ in range(values_len)]
        _type = int(input("Enter the vector type: "))

        self.controller.update_by_name_id_ctrl(
            name=name, name_id=name_id, color=color, values=values, _type=_type
        )

    def delete_by_index_submenu(self):
        """
        Delete vector by index
        """
        self.controller.delete_by_index_ctrl(int(input("Enter index: ")))

    def delete_by_name_submenu(self):
        """
        Delete vector by name id
        """
        self.controller.delete_by_name_ctrl(input("Enter name: "))

    def plot_submenu(self):
        """
        Plot all vectors using matplotlib
        """
        pass

    def get_repository_elements_sum_submenu(self):
        """
        Get the sum of all elements of all vectors in the repository
        """
        print(self.controller.get_repository_elements_sum_ctrl())

    def get_repository_vector_sum_submenu(self):
        """
        Get the sum of all vectors in the repository as a vector
        """
        print(self.controller.get_repository_vector_sum_ctrl())

    def get_vectors_that_have_sum_submenu(self):
        """
        Get a list of vectors having the sum equal to the given value
        """
        expected_sum = int(input("Enter the expected sum: "))
        vectors = self.controller.get_vectors_that_have_sum_ctrl(expected_sum)

        print("\n".join([str(v) for v in vectors]))

    def get_vectors_with_min_less_than_submenu(self):
        """
        Get a list of vectors having the mininum less than the given
        value
        """
        print(
            self.controller.get_vectors_with_min_less_than_ctrl(
                int(input("Enter minimum limit: "))
            )
        )

    def get_vectors_with_color_submenu(self):
        """
        Get the sum of elements of vectors that have the given color
        """
        print(self.controller.get_vectors_with_color_ctrl(input("Enter color: ")))

    def get_sum_of_vectors_with_sum_gt_submenu(self):
        """
        Get the sum of elements of vectors that have sum greater than a value
        """
        print(
            self.controller.get_sum_of_vectors_with_sum_gt_ctrl(
                int(input("Enter sum: "))
            )
        )

    def get_min_of_all_vectors_submenu(self):
        """
        Return the minimum of all vectors
        """
        print(self.controller.get_min_of_all_vectors_ctrl())

    def get_dot_product_of_consecutive_vectors_submenu(self):
        """
        Get the dot product of consecutive vectors in the array
        """
        print(self.controller.get_dot_product_of_consecutive_vectors_ctrl())

    def delete_all_vectors_submenu(self):
        """
        Empty the vector repository
        """
        self.controller.delete_all_vectors_ctrl()

    def delete_by_color_submenu(self):
        """
        Delete vectors that have a given color
        """
        self.controller.delete_by_color_ctrl(input("Enter color: "))

    def delete_by_prod_submenu(self):
        """
        Delete all vectors that have a product greater than a given
        """
        self.controller.delete_by_prod_ctrl(int(input("Enter product: ")))

    def delete_between_indexes_submenu(self):
        """
        Delete vectors between two indexes
        """
        self.controller.delete_between_indexes_ctrl(
            int(input("Enter starting index: ")), int(input("Enter ending index: "))
        )

    def delete_by_max_value_submenu(self):
        """
        Delete vectors that have a given maximum value
        """
        self.controller.delete_by_max_value_ctrl(
            input("Enter maximum value to delete by: ")
        )

    def add_to_all_submenu(self):
        """
        Add a scalar to all vectors
        """
        self.controller.add_to_all_ctrl(int(input("Enter scalar: ")))

    def update_color_by_name_submenu(self):
        """
        Update the color of a vector identified by a given name
        """
        self.controller.update_color_by_name_ctrl(
            input("Enter name: "), input("Enter color: ")
        )

    def update_by_type_set_color_submenu(self):
        """
        Update all vectors of a given type by changing their color
        """
        self.controller.update_by_type_set_color_ctrl(
            int(input("Enter type: ")), input("Enter color")
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
