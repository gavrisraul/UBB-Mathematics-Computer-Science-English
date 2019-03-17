#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
2.Find the minimum and maximum of a list.
"""

def Solution(ls, n):
    ls = []
    mn = 9999
    mx = -9999
    for i in range(0, n):
        nr = int(input())
        ls.append(nr)
        if nr > mx:
            mx = nr
        if nr < mn:
            mn = nr
    print mx, mn

n = int(input())
ls = []
Solution(ls, n)

