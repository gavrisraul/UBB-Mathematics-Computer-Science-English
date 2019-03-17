#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""

"""

class StudentObj(object):

    def __init__(self, idd, name, grade):
        self.idd = idd
        self.name = name
        self.grade = grade

    def get_idd(self):
        return self.idd

    def set_idd(self, idd):
        self.idd = idd

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return str(self.idd) + " " + self.name + " " + str(self.grade)

