#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
9.Print all numbers with maximum 2 digits of form xy with the property that
the last digit of (xy) 2 is y.
Example: 5 2 =25 or (10) 2 =100 or (76) 2 =5776.
"""
import math


for i in range(0, 100):
    if i % 10 == int(math.pow(i, 2)) % 10:
        print i, i * i
