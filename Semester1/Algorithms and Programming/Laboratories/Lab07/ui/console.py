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
from domain.point import MyPoint


class Ui(object):
    """
    Ui Class
    """

    def __init__(self):
        """
        Constructor for Ui Class
        """
        self.controller = Controller()
        self.options = {
            1: self.add_by_coords_submenu,
            2: self.add_by_color_submenu,
            3: self.get_all_submenu,
            4: self.get_by_index_submenu,
            5: self.get_by_color_submenu,
            5: self.get_by_color_submenu,
            6: self.get_points_in_square_submenu,
            7: self.get_points_in_rectangle_submenu,
            8: self.get_points_in_circle_submenu,
            9: self.get_min_dist_submenu,
            10: self.get_max_dist_submenu,
            11: self.update_point_at_index_submenu,
            12: self.update_point_color_submenu,
            13: self.shift_all_on_x_submenu,
            14: self.shift_all_on_y_submenu,
            15: self.delete_by_index_submenu,
            16: self.delete_by_coords_submenu,
            17: self.delete_inside_square_submenu,
            18: self.plot_all_in_chart_submenu,
            19: self.exit_submenu,
        }

    def add_by_coords_submenu(self):
        """
        Add by coords submenu
        """
        coord_x = int(input("coord x: "))
        coord_y = int(input("coord y: "))
        color = input("color: ")
        self.controller.add_point_by_coords_ctrl(MyPoint(coord_x, cooord_y, color))

    def add_by_color_submenu(self):
        """
        Add by color submenu
        """
        coord_x = int(input("coord x: "))
        coord_y = int(input("coord y: "))
        color = input("color: ")
        self.controller.add_point_by_color_ctrl(MyPoint(coord_x, cooord_y, color))

    def get_all_submenu(self):
        """
        Get all submenu
        """
        self.controller.get_all_ctrl()

    def get_by_index_submenu(self):
        """
        Get by index submenu
        """
        index = int(input("index: "))
        self.controller.get_by_index_ctrl(index)

    def get_by_color_submenu(self):
        """
        Get by color submenu
        """
        color = input("color: ")
        self.controller.get_by_color_ctrl(color)

    def get_points_in_square_submenu(self):
        """
        Get points in square submenu
        """
        upper_x = int(input("upper x: "))
        upper_y = int(input("upper y: "))
        length = int(input("length: "))
        self.controller.get_points_in_square_ctrl(upper_x, upper_y, length)

    def get_points_in_rectangle_submenu(self):
        """
        Get points in rectangle submenu
        """
        upper_x = int(input("upper x: "))
        upper_y = int(input("upper y: "))
        length = int(input("length: "))
        width = int(input("width: "))
        self.controller.get_points_in_rectangle_ctrl(upper_x, upper_y, length, width)

    def get_points_in_circle_submenu(self):
        """
        Get points in circle submenu
        """
        centerx = int(input("centerx: "))
        centery = int(input("centery: "))
        radius = int(input("radius: "))
        self.controller.get_points_in_circle_ctrl(centerx, centery, radius)

    def get_min_dist_submenu(self):
        """
        Get min distance submenu
        """
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        self.controller.get_min_dist_ctrl(x1, y1, x2, y2)

    def get_max_dist_submenu(self):
        """
        Get max distance submenu
        """
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        self.controller.get_max_dist_ctrl(x1, y1, x2, y2)

    def update_point_at_index_submenu(self):
        """
        Update point at index submenu
        """
        index = int(input("index: "))
        x = int(input("x: "))
        y = int(input("y: "))
        color = input("color: ")
        self.controller.update_point_at_index_ctrl(index, x, y, color)

    def update_point_color_submenu(self):
        """
        Update point color submenu
        """
        x = int(input("x: "))
        y = int(input("y: "))
        color = input("color: ")
        self.controller.update_point_color_ctrl(x, y, color)

    def shift_all_on_x_submenu(self):
        """
        Shift all on x submenu
        """
        value = int(input("value: "))
        self.controller.shift_all_on_x_ctrl(value)

    def shift_all_on_y_submenu(self):
        """
        Shift all on y submenu
        """
        value = int(input("value: "))
        self.controller.shift_all_on_y_ctrl(value)

    def delete_by_index_submenu(self):
        """
        Delete by index submenu
        """
        index = int(input("index: "))
        self.controller.delete_by_index_ctrl(index)

    def delete_by_coords_submenu(self):
        """
        Delete by coords submenu
        """
        x = int(input("x: "))
        y = int(input("y: "))
        self.controller.delete_by_coords_ctrl(x, y)

    def delete_inside_square_submenu(self):
        """
        Delete inside square submenu
        """
        length = int(input("length: "))
        self.controller.delete_inside_square_ctrl(length)

    def plot_all_in_chart_submenu(self):
        """
        Plot al points in chart submenu
        """
        self.controller.plot_all_in_chart_ctrl()

    def exit_submenu(self):
        """exit the app"""
        exit()

    def run(self):
        """
        run the app and cycle through options
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
