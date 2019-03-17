#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
6.Given the current date (day, month, year) and the birthdate of a person
(day, month, year) compute the age of the person in number of years.
Example: If the current date is 4.3.2002 and the person birthdate is
5.9.1980 than the person is 21 years old.
"""

cD = int(input("Current day: "))
cM = int(input("Current month: "))
cY = int(input("Current year: "))

pD = int(input("Person day: "))
pM = int(input("Person month: "))
pY = int(input("Person year: "))

if cM - pM > 0:
    print cY - pY
elif cM - pM < 0:
    print cY - pY - 1
else:
    if cD - pD >= 0:
        print cY - pY
    else:
        print cY - pY - 1
