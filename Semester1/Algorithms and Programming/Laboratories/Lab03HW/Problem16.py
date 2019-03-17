#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
16.Read numbers having minimum 2 digits until number 0 is given. Print how
many numbers have the unit figure smaller than the tens figure.
Example: If numbers read are 25, 653, 2965, 211, 154, 1256, 0 value 3 will
be displayed.
"""

n1 = int(input())
i = 0
while n1 != 0:
    if n1 % 10 < n1 / 10 % 10:
        i += 1
    n1 = int(input())

print i
