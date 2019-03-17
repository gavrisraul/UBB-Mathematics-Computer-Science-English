#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
2.Determine if a given number n is prime or not.
Example: n = 3 is prime, but n = 6 is not prime
"""
import math  # for sqrt


def IsPrime(n):
    """Check if number is prime"""
    if n == 0 or n == 1:
        return 0
    else:
        for d in range(2, int(math.sqrt(n) + 1)):
            if n % d == 0:
                return 0
    return 1


n = int(input("Give number: "))
if IsPrime(n) == 1:
    print(n, "is prime")
else:
    print(n, "is not prime")
