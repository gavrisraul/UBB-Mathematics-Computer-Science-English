#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
1.Compute the sum of two given numbers.
"""


def Sum(a, b):
    """Function for sum of 2 numbers"""
    return a + b


a = int(input("Give first number: "))
b = int(input("Give second number: "))
print("The sum is: ", Sum(a, b))
