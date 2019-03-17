#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
2.Compute the product of the first n natural numbers.
"""


def Prod(n):
    """Function for product untill n"""
    if n == 1:
        return 1
    else:
        return n * Prod(n - 1)


n = int(input("Give number: "))
print("The product of first n numbers is: ", Prod(n))
