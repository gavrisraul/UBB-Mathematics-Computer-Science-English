#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
20.Given a natural number n, determine the greatest number p having the
property that 2^p is smaller or equal to n.
Example: For n=133, the result is p=7 (2^7 =128, 2^8 =256).
"""

import math

n = int(input())

p = 0

while int(math.pow(2, p + 1)) <= n:
    p += 1

print(p)
