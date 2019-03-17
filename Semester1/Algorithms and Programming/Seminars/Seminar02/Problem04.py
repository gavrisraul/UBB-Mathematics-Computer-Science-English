#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
4.Given two integers, verify if they are “friends”. Two numbers are friends if each
number equals the sum of divisors of the other number. Example: 220 and 284
are friends because 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284 and 1
+ 2 + 4 + 71 + 142 = 220
"""

def SumofDiv(n):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s += d
    return s

n1 = int(input())
n2 = int(input())

if SumofDiv(n1) == n2 and SumofDiv(n2) == n1:
    print "numbers are friends"
else:
    print "numbers are not friends"
