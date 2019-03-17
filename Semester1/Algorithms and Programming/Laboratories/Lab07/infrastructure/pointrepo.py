#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
PointRepository class
"""

import matplotlib.pyplot as plt
import math
from domain.point import MyPoint


class PointRepository(object):
    """
    PointRepository class
    """

    colors = ["red", "green", "blue", "yellow", "magenta"]

    def __init__(self):
        """
        Initialization for PointRepository class.It takes only a list
        """
        self.points = []

    def addnewbycolor(self, newpoint):
        """
        addnewbycolor(newpoint). Adds a new point to the main list if it has the corresponding color
        """
        ok = 0
        for i in range(0, len(self.colors)):
            if self.colors[i] == newpoint.get_color():
                ok = 1
        if ok == 1:
            self.points.append(newpoint)
        else:
            raise ValueError("No such color")

    def addnewbycoords(self, newpoint):
        """
        addnewbycoords(newpoint). Adds a new point to the main list if it has coords different from all the points given
        """
        ok = 1
        for i in range(0, len(self.points)):
            if (self.points[i].get_coord_x() == newpoint.get_coord_x()) and (
                self.points[i].get_coord_y() == newpoint.get_coord_y()
            ):
                ok = 0
        if ok == 1:
            self.points.append(newpoint)
        else:
            raise ValueError("Point exists")

    def getallpoints(self):
        """
        getallpoints() .It gets all the points given
        """
        return self.points

    def getbyindex(self, index):
        """
        getbyindex(index) .It gets a point at a given index
        """
        if index >= 0 and index < len(self.points):
            return self.points[index]
        else:
            raise ValueError("Index out of range...try again")

    def getbycolor(self, color):
        """
        getbycolor(color) . It gets all the points for a given color
        """
        l = []
        for i in range(0, len(self.points)):
            if self.points[i].get_color() == color:
                l.append(self.points[i])
        return l

    def getpointsinsquare(self, upper_x, upper_y, length):
        """
        get points in square
        """
        l = []
        for i in range(0, len(self.points)):
            if (
                self.points[i].get_coord_x() >= upper_x
                and self.points[i].get_coord_y() <= upper_y
            ) and (
                self.points[i].get_coord_x() < length
                and self.points[i].get_coord_y() < length
            ):
                l.append(self.points[i])
        return l

    def getpointsinrectangle(self, upper_x, upper_y, length, width):
        """
        get points in rectangle
        """
        l = []
        for i in range(0, len(self.points)):
            if (
                self.points[i].get_coord_x() >= upper_x
                and self.points[i].get_coord_y() <= upper_y
            ) and (
                self.points[i].get_coord_x() < width
                and self.points[i].get_coord_y() < length
            ):
                l.append(self.points[i])
        return l

    def getpointsincircle(self, centerx, centery, radius):
        """
        getpointsincircle(center, radius) . It gets all the points in the circle
        """
        l = []
        for i in range(0, len(self.points)):
            distCenterPoint = math.sqrt(
                math.pow((self.points[i].get_coord_x() - centerx), 2)
                + math.pow((self.points[i].get_coord_y() - centery), 2)
            )
            if distCenterPoint <= radius:
                l.append(self.points[i])
        return l

    def getmindist(self, x1, y1, x2, y2):
        """
        getmindist(x1, y1, x2, y2) .It gets the minimum distance between 2 points
        """
        return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

    def getmaxdist(self, x1, y1, x2, y2):
        """
        getmaxdist(x1, y1, x2, y2) .It gets the maximum distance between 2 points
        """
        if y1 > y2 and x1 > x2:
            return (y1 - y2) + (x1 - x2)
        elif y2 > y1 and x2 > x1:
            return (y2 - y1) + (x2 - x1)

    def updatepointatindex(self, index, x, y, color):
        """
        updates a point at a given index
        """
        self.points[index] = MyPoint(x, y, color)

    def updatepointcolor(self, x, y, color):
        """
        updates a point's color at given coords
        """
        for i in range(0, len(self.points)):
            if self.points[i].get_coord_x() == x and self.points[i].get_coord_y() == y:
                self.points[i].set_color(color)

    def shiftallonx(self, value):
        """
        shiftallonx(value) .It shifts all points on x axis
        """
        l = []
        for i in range(0, len(self.points)):
            self.points[i].set_coord_x(self.points[i].get_coord_x() + value)
            l.append(self.points[i])
        return l

    def shiftallony(self, value):
        """
        shiftallony(value) .It shifts all points on y axis
        """
        l = []
        for i in range(0, len(self.points)):
            self.points[i].set_coord_y(self.points[i].get_coord_y() + value)
            l.append(self.points[i])
        return l

    def deletebyindex(self, index):
        """
        deletebyindex(index) .It deltes and element at a given index
        """
        if index >= 0 and index < len(self.points):
            del (self.points[index])
        else:
            raise ValueError("Index out of range...try again")

    def deletebycoords(self, x, y):
        """
        detele a point by its coordinates
        """
        for i in range(0, len(self.points)):
            if self.points[i].get_coord_x() == x and self.points[i].get_coord_y() == y:
                del (self.points[i])

    def delteinsidesquare(self, length):
        """
        delte points in a square
        """
        l = []
        for i in range(0, len(self.points)):
            if (
                self.points[i].get_coord_x() <= upper_x
                and self.points[i].get_coord_y() >= upper_y
            ) and (
                self.points[i].get_coord_x() > length
                and self.points[i].get_coord_y() > length
            ):
                l.append(self.points[i])
        return l

    def plotallinchart(self):
        """
        It plots all points in a chart
        """
        for i in range(0, len(self.points)):
            plt.scatter(
                self.points[i].get_coord_x(),
                self.points[i].get_coord_y(),
                c=self.points[i].get_color(),
            )
        plt.show()

    def __repr__(self):
        """
        Representation for the list
        """
        return str(self.points)

    def __str__(self):
        """
        Representation for the list
        """
        return str(self.points)


# v = PointRepository()
# pt = point.MyPoint(1, 2, "red")
# v.addnewbycoords(pt)
# pt = point.MyPoint(2, 4, "magenta")
# v.addnewbycoords(pt)
# pt = point.MyPoint(3, 3, "ha")
# v.addnew(pt)
# pt = point.MyPoint(1, 4, "red")
# v.addnewbycoords(pt)
# print(v.getbycolor("red"))
# print(v)
# v.shiftallonx(2)
# v.deletebyindex(1)
# print(v)
# print(v.getpointsincircle(0, 0, 3))


# x = [1, 2, 3]
# y = [1, 2, 3]
# col = ["red", "green", "blue"]
# plt.scatter(x, y, c=col)
# plt.show()
