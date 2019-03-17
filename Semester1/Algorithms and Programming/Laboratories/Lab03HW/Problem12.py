#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
12.Determine if two natural numbers have the following property: the same
digits are necessary to write them in base 10.
Example: 2113 and 31221 have this property, whereas 12521 and 11551
do not.
"""

n1 = int(input())
n2 = int(input())

s1 = set()
s2 = set()

while n1 != 0:
    dig1 = n1 % 10
    s1.add(dig1)
    n1 /= 10

while n2 != 0:
    dig2 = n2 % 10
    s2.add(dig2)
    n2 /= 10

if sorted(s1) == sorted(s2):
    print "is ok"
else:
    print "not ok"
