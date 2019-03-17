#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
11.Generate all prime numbers having n digits with the property that all its
prefixes are also prime.
Example: For n=2 the first number is 23 (2, 23 are primes).
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


def Nr(n):
    """Compute the number of digits of a number"""
    nr = 0
    while n != 0:
        nr += 1
        n /= 10
    return nr


def Verify(n):
    """Verify if digit is prime"""
    while n != 0:
        if IsPrime(n) == 0:
            return False
        n /= 10
    return True


n = int(input())

i = 1
while Nr(i) <= n:
    if Nr(i) == n:
        if Verify(i) == True:
            print(i)
    i += 1
