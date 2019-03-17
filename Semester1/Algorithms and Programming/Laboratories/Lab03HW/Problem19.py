#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
19.Print the numbers of n digits equal to k multiplied by their product.
Numbers n and k (n between 1 and 9, k between 1 and 1000) are given.
Example: For n=3 and k=5 the only number that satisfies the requested
properties is 175 (5*(1*7*5)).
"""


def Nr(n):
    """Number of digits"""
    s = 0
    while n != 0:
        s += 1
        n /= 10
    return s


def DigProd(n):
    """Digits product"""
    p = 1
    while n != 0:
        cif = n % 10
        p = p * cif
        n /= 10
    return p


n = int(input())
k = int(input())

a = 1

while Nr(a) <= n:
    if Nr(a) == n:
        if DigProd(a) * k == a:
            print a
    a += 1
