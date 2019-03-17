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

from infrastructure.pointrepo import PointRepository
from domain.point import MyPoint


class Controller(object):
    """
    Controller class
    """

    def __init__(self):
        """
        constructor for controller class
        """
        self.repo = PointRepository()

    def add_point_by_color_ctrl(self, newpoint):
        """
        Add point by color
        """
        self.repo.addnewbycolor(newpoint)

    def add_point_by_coords_ctrl(self, newpoint):
        """
        Add point by coords
        """
        self.repo.addnewbycoords(newpoint)

    def get_all_ctrl(self):
        """
        Gets all points
        """
        self.repo.getallpoints()

    def get_by_index_ctrl(self, index):
        """
        Get by index
        """
        self.repo.getbyindex(index)

    def get_by_color_ctrl(self, color):
        """
        Get by color
        """
        self.repo.getbycolor(color)

    def get_points_in_square_ctrl(self, upper_x, upper_y, length):
        """
        Get points in square
        """
        self.repo.getpointsinsquare(upper_x, upper_y, length)

    def get_points_in_rectangle_ctrl(self, upper_x, upper_y, length, width):
        """
        Get points in rectangle
        """
        self.repo.getpointsinrectangle(upper_x, upper_y, length, width)

    def get_points_in_circle_ctrl(self, centerx, centery, radius):
        """
        Get points in circle
        """
        self.repo.getpointsincircle(centerx, centery, radius)

    def get_min_dist_ctrl(self, x1, y1, x2, y2):
        """
        Get min distance
        """
        self.repo.getmindist(x1, y1, x2, y2)

    def get_max_dist_ctrl(self, x1, y1, x2, y2):
        """
        Get max distance
        """
        self.repo.getmaxdist(x1, y1, x2, y2)

    def update_point_at_index_ctrl(self, index, x, y, color):
        """
        Update point at index
        """
        self.repo.updatepointatindex(index, x, y, color)

    def update_point_color_ctrl(self, x, y, color):
        """
        Update point color
        """
        self.repo.updatepointcolor(x, y, color)

    def shift_all_on_x_ctrl(self, value):
        """
        Shift all on x
        """
        self.repo.shiftallonx(value)

    def shift_all_on_y_ctrl(self, value):
        """
        Shift all on y
        """
        self.repo.shiftallony(value)

    def delete_by_index_ctrl(self, index):
        """
        Delete by index
        """
        self.repo.deletebyindex(index)

    def delete_by_coords_ctrl(self, x, y):
        """
        Delete by coords
        """
        self.repo.deletebycoords(x, y)

    def delete_inside_square_ctrl(self, length):
        """
        delete inside square
        """
        self.repo.delteinsidesquare(length)

    def plot_all_in_chart_ctrl(self):
        """
        Plot all points in chart
        """
        self.repo.plotallinchart()
