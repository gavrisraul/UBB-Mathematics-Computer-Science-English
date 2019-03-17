#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
7.Return the number of even integers in a list.
"""

def Solution(ls, n):
    j = 0
    ls = []
    for i in range(0, n):
        nr = int(input())
        ls.append(nr)

    for i in range(0, n):
        if ls[i] % 2 == 0:
            j += 1
    return j
n = int(input())
ls = []
print Solution(ls, n)

