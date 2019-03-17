#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
3.Print all powers less than k of a given integer number n.
Example: For n=5 and k=100, print the numbers 1, 5, 25.
"""
import math

n = int(input("Give number: "))
k = int(input("Give k: "))

i = 0
while i < k:
    if math.pow(n, i) <= k:
        print(int(math.pow(n, i)))
    i += 1
