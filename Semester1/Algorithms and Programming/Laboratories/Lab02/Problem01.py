#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
1.Compute the sum of all even numbers less or equal to a given number n.
Example: n = 7, sum is 0 + 2 + 4 + 6 = 12 and the result should be the message “The
sum of even numbers up to 7 is 12.”.
"""
n = int(input("Give n: "))
s = 0
for nr in range(0, n + 1, 2):
    s = s + nr
print("The sum of even numbers up to ", n, " is ", s)
