#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
sys.path.append("../Student/")
import student

class StudentRepo(object):
    def __init__(self):
        self.students = []

    def addnew(self, st):
        for e in self.students:
            if e.get_idd() == st.get_idd():
                raise ValueError("id is existing...")
        self.students.append(st)

    def size(self):
        return len(self.students)

    def __str__(self):
        return str(self.students)

idd = int(input())
name = input()
grade = int(input())

var = StudentRepo()
st = student.StudentObj(idd, name, grade)
var.addnew(st)

print(str(var) + "\n")

idd = int(input())
name = input()
grade = int(input())

st = student.StudentObj(idd, name, grade)
var.addnew(st)

print(str(var) + "\n")

print(var.size())
