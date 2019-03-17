#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
2.Compute the sum of the first n natural numbers.
"""

n = int(input())
s = 0
for i in range(0,n+1):
    s += i
print s
