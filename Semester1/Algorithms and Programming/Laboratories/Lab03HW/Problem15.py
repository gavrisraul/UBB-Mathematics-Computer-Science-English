#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
15.Determine the age of a person in number of days. The current date and
the birthdate are known.
Example: If the birthdate is 1.1.2009 and the current date is 28.9.2009
than the person has 271 days.
"""
cD = int(input("Current day: "))
cM = int(input("Current month: "))
cY = int(input("Current year: "))

pD = int(input("Person day: "))
pM = int(input("Person month: "))
pY = int(input("Person year: "))

S = (cY - pY) * 365 + (cM - pM) * 31 + (cD - pD)
print S
