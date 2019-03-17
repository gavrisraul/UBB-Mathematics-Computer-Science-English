#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
1.Compute the control digit of an integer by summing up its digits, then
summing up the digits of the sum, so on, until a sum of only one digit is
obtained.
Example: The control digit of integer number 1971 is 9 (1971  18  9).
"""

n = int(input("Give number: "))
aux = n
while n > 9:
    s = 0
    while n != 0:
        s = s + n % 10
        n = n / 10
    n = s
    # print(n)
print "The control digit of integer number ", aux, " is ", s
