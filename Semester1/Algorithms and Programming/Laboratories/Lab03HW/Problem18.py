#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
18.Print the number of common digits of two numbers, as well as the digits.
Example: 21348 and 14513 have 3 common digits and they are 1,3,4.
"""

n1 = int(input())
n2 = int(input())
mySet = set()
cop1 = n1
cop2 = n2
while cop1 != 0:
    cop2 = n2
    while cop2 != 0:
        if cop1 % 10 == cop2 % 10:
            mySet.add(cop1 % 10)
        cop2 /= 10
    cop1 /= 10

print mySet, len(mySet)
