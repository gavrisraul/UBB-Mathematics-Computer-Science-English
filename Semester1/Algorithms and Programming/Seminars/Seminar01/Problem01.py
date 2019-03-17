#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
1.Given 2 integers, return True if one of them is 10 or if their sum is 10.
"""

def make_ten(a, b):
    if (a == 10 or b == 10) or a+b == 10:
        return True
    return False

a = int(input("first number: "))
b = int(input("second number: "))

print make_ten(a, b)
