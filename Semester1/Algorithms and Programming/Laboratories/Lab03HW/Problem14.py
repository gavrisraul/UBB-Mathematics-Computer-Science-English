#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
14.Read a natural number n. Print the number of 1s from the binary
representation of n.
Example: 547 has 4 digits equal to 1 in its binary representation.
"""
n10 = int(input())
p = 1
n2 = 0
while n10 != 0:
    r = n10 % 2
    n2 = n2 + r * p
    p = p * 10
    n10 = n10 / 2
nr = 0
while n2 != 0:
    dig = n2 % 10
    if dig == 1:
        nr += 1
    n2 /= 10
print nr
