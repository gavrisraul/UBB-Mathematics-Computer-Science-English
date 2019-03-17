#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
1.Compute the sum of n numbers given as a list. Modify the function to exclude
number 12 from the sum.
"""

def Solution(ls, n):
    ls = []
    s = 0
    for i in range(0, n):
        nr = int(input())
        ls.append(nr)
        if nr != 12:
            s = s + nr
    return s

n = int(input())
ls = []
print Solution(ls, n)
