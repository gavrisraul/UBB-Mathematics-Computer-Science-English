#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
6.Given 2 strings, return the number of the positions where the two strings contain
the same substring of length 2. Example: "xxcaazz" and "xxbaaz" yield 3, since the
"xx", "aa", and "az" substrings appear in the same place in both strings.
"""
import math

def MIN(a, b):
    if(a < b):
        return a
    else:
        return b

a = raw_input()
b = raw_input()

def Counting(nr):
    nr = 0
    for i in range(MIN(len(a), len(b))):
        if a[i : i + 2] == b[i : i + 2]:
            nr += 1
    return nr

nr = 0
print Counting(nr)
