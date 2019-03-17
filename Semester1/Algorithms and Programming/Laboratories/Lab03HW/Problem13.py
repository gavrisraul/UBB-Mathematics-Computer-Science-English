#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
13.Read a natural number. Form another number from its digits found at odd
positions (from left to right).
Example: For 1234, the result is 13.
"""


def Solve(n):
    """Solution: form a new number with the given condition at digit for i"""
    i = 0
    cop = n
    nou = 0
    p = 1
    while cop != 0:
        cif = cop % 10
        if i % 2 != 0:
            nou = nou + cif * p
            p = p * 10
        i += 1
        cop /= 10
    return nou


n = int(input())
print(Solve(n))
