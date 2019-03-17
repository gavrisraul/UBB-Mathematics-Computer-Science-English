#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
3.Transform an array into a set.
"""

ls = []
n = int(input())
for i in range(0, n):
    nr = int(input())
    ls.append(nr)

newls = []

for i in range(0, n):
    if ls[i] not in newls:
        newls.append(ls[i])

print newls
