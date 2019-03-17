#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
4.Find the highest prime number, smaller than a given n.
"""

import math

def IsPrime(n):
    if n == 0 or n == 1:
        return 0
    else:
        for d in range(2, int(math.sqrt(n)+1)):
            if n%d == 0:
                return False
    return True

def FindIt(n):
    aux = n - 1
    while IsPrime(aux) == False:
        aux -= 1
    return aux

n = int(input())

print FindIt(n)
