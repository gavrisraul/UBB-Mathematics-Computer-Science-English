#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
8.Consider an integer number n. Print the nearest prime number to n.
Example: For n=22, the result is 23, whereas for n=20, the result is 19.
"""
import math


def IsPrime(n):
    """Check if number is prime"""
    if n == 0 or n == 1:
        return 0
    else:
        for d in range(2, int(math.sqrt(n) + 1)):
            if n % d == 0:
                return 0
    return 1


n = int(input())

a = n + 1
b = n - 1
while IsPrime(a) == False:
    a += 1
while IsPrime(b) == False:
    b -= 1

if a - n < n - b:
    print(a)
else:
    print(b)
