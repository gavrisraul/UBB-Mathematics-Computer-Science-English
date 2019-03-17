#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
2.Determine a date (as day, month, year) starting from two integer
numbers that represent the year and the number of the day in that year.
Example: For year = 2004 and number of day = 68, the date is 8.03.2004
"""

year = int(input("Give year: "))
day = int(input("Give day: "))

print("The date is ", day - int(day / 30) * 30, ".", int(day / 30) + 1, ".", year)
