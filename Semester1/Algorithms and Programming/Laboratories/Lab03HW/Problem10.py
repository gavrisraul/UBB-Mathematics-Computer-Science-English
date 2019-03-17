#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
10.Read integers numbers until number 0 is read. Print the number of pairs
n1 and n2 of numbers read consecutively with the property that the
number of digits 5 from n1 is strictly higher than the number of digits 5
from n2.
Example: If the numbers read are 182, 457,341, 497, 5597, 1335, 15, 38,
5, 0 than the result is 3 (as the pairs 457-341, 5597-1335, 15-38 satisfy the
required property).
"""

n1 = int(input())

aux = 0
while n1 != 0:
    n2 = int(input())
    if n2 != 0:
        copn2 = n2
        copn1 = n1
        nrn1 = 0
        nrn2 = 0
        while copn2 != 0:
            if copn2 % 10 == 5:
                nrn2 += 1
            copn2 /= 10
        while copn1 != 0:
            if copn1 % 10 == 5:
                nrn1 += 1
            copn1 /= 10
        if nrn1 > nrn2:
            aux += 1
    n1 = n2

print "result", aux
