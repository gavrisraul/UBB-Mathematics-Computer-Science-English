#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
17.A number n is special if there is a natural number m such that n=m+S(m)
where S(m) is the sum of digits of m. Verify if a given number is special.
Example: 1235 is special (1235=1225+10)
"""

n = int(input())
a = 1
ok = 0
while ok == 0 and a <= n:
    cop = a
    s = 0
    while cop != 0:
        s = s + cop % 10
        cop /= 10
    if s + a == n:
        print a, "+", s, "number:", n, "is special"
        ok = 1
    a += 1
