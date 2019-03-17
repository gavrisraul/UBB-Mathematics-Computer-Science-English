#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
7.Generate in ascending order the first n numbers from the set M defined
as:
a. Number 1 belongs to M
b. If x belongs to M then 2x+1 and 3x+1 also belong to M
c. M does not contain any other elements
Example: The first 10 numbers in M are 1, 3, 4, 7, 9, 10, 13, 15, 19, 21.
"""

v = []

n = int(input())

i = 1
j = 1
v.append(i)
while j <= n:
    a = 2 * i + 1
    b = 3 * i + 1
    v.append(a)
    v.append(b)
    i = v[j]
    j += 1
v.sort()
print v[:n]
